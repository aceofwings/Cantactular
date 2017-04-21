#! python3
#Courtesy of Shane Firmware Team
"""
    File:       dbcParser.py
    Created:    03/29/2017

    This Python script contains classes for describing the contents of a CAN
    database file. Given a .dbc file, it will parse it into objects in memory
    and generate a C header file for use by the Network Manager embedded
    firmware application for packaging and unpackaging data in CAN data frames.

    Before editing, please read the EVT Wiki page describing the objects in a
    CAN Database, located here:
        https://wiki.rit.edu/display/EVT/CAN+Database
"""

import re
from enum import Enum
from gateway.utils.projectpaths import ProjectPath

__regex_pattern__ = re.compile(r""" SG_ (?P<name>.*) : (?P<start_bit>[0-9]{1,2})\|(?P<length>[0-9]{1,2})@(?P<format>[0-1])(?P<type>[+-]) \((?P<factor>.*),(?P<offset>.*)\) \[(?P<min>.*)\|(?P<max>.*)\] "(?P<unit>.*)" Vector__XXX""")


class CANDatabase:
    """
    Object to hold all CAN messages in a network as defined by the DBC file.
    """

    # Private Properties
    _name = ""
    _dbcPath = ""
    _comment = ""
    _messages = list()
    _txNodes = dict()
    _extended = False
    _attributes = list()
    _iter_index = 0

    def __init__(self, fileName):
        """
        Constructor for the CAN Database.

        Arguments:
         - dbcPath: The file path to .dbc file.
        """
        self._dbcPath = ProjectPath().edsfile(fileName)

    def __iter__(self):
        """
        Defined to make the object iterable.
        """
        return self

    def __next__(self):
        """
        Get the next iterable in the CANMessage list.
        """
        if self._iter_index == len(self._messages):
            self._iter_index = 0
            raise StopIteration
        self._iter_index += 1
        return self._messages[self._iter_index-1]

    def Load(self):
        """
        Opens the DBC file and parses its contents.
        """
        try:
            file = open(self._dbcPath)
        except OSError:
            print("Invalid file path specified.")
            return

        building_message = False
        can_msg = None

        line_number = 0
        for line in file:
            line = line.rstrip('\n')
            line_number += 1  # keep track of the line number for error reporting

            if line.startswith("BU_:"):
                self._parseTransmittingNodes(line)

            elif line.startswith("BO_"):
                can_msg = self._parseMessageHeader(line).ResetSignals().ResetAttributes()
                building_message = True

            elif line.startswith(" SG_") and building_message:
                can_msg.AddSignal(self._parseSignalEntry(line))

            elif line == "":
                if building_message:
                    building_message = False
                    self._txNodes[can_msg._txNode] += [can_msg]
                    can_msg = None

            # elif line[0:3] == "CM_":
                #  self._parseComment(line)

            elif line.startswith("VAL_"):
                val_components = valueLineSplit(line)
                new_value_name = val_components[2]
                new_value_canID = int(val_components[1], 16)
                # Tuple: (Name, CAN ID, Item Pairs)
                new_value = (new_value_name, new_value_canID, list())

                pairs = val_components[3:]
                for i in range(0, len(pairs), 2):
                    try:
                        # add item value/name pairs to list in new_value tuple
                        item_value = int(pairs[i])
                        item_name = pairs[i+1]
                        new_value[2].append((item_value, item_name))
                    except IndexError:
                        print("Invalid value: " + new_value_name +
                              ". Found on line " + str(line_number) + '.')
                        return None

                for message in self:
                    if message.CANID() == new_value[1]:
                        message.AddValue(new_value)
                        break

            # parse attributes
            elif line.startswith("BA_DEF_ BO_"):
                components = line.split(' ')
                # warning: indices are one higher than they appear to be because of double space in line
                attr_name = components[3].strip('"')
                attr_type = components[4]
                attr_min = components[5]
                attr_max = components[6].rstrip(';')

                new_attr = (attr_name, attr_type, attr_min, attr_max)
                self._attributes.append(new_attr)

            elif line.startswith("BA_ "):
                components = line.split(' ')
                attr_name = components[1].strip('"')
                attr_msgID = int(components[3], 16)
                attr_val = components[4].rstrip(';')

                new_attr = (attr_name, attr_msgID, attr_val)

                for message in self:
                    if message.CANID() == attr_msgID:
                        message.AddAttribute(new_attr)
                        break

        return self

    def Name(self):
        """
        Gets the CAN Database's name.
        """
        return self._name

    def Messages(self):
        """
        Gets the list of CANMessage objects.
        """
        return self._messages

    def _parseTransmittingNodes(self, line):
        """
        Takes a string and parses the name of transmitting nodes in the CAN bus
        from it.
        """
        items = line.split(' ')
        for each in items:
            if each == "BU_:":
                pass
            else:
                self._txNodes.setdefault(each, [])
        return

    def _parseMessageHeader(self, line):
        """
        Creates a signal-less CANMessage object from the header line.
        """
        items = line.split(' ')
        # converts to an integer from the hexadecimal number
        msg_id = int(items[1])
        msg_name = items[2].rstrip(':')
        msg_dlc = int(items[3])
        msg_tx = items[4].rstrip('\n')

        return CANMessage(msg_id, msg_name, msg_dlc, msg_tx)

    def _parseSignalEntry(self, line):
        """
        Creates a CANSignal object from DBC file information.

        The Regex used is compiled once in order to save time for the numerous
        signals being parsed.
        """
        result = __regex_pattern__.match(line)

        name = result.group('name')
        start_bit = int(result.group('start_bit'))
        length = int(result.group('length'))
        sig_format = int(result.group('format'))
        sig_type = result.group('type')
        factor = int(result.group('factor'))
        offset = int(result.group('offset'))
        minimum = int(result.group('min'))
        maximum = int(result.group('max'))
        unit = result.group('unit')

        return CANSignal(name, sig_type, sig_format, start_bit, length, offset,
                         factor, minimum, maximum, unit)


class CANMessage:
    """
    Contains information on a message's ID, length in bytes, transmitting node,
    and the signals it contains.
    """
    _name = ""
    _canID = None
    _idType = None
    _dlc = 0
    _txNode = ""
    _comment = ""
    _signals = list()
    _attributes = list()
    _iter_index = 0

    def __init__(self, msg_id, msg_name, msg_dlc, msg_tx):
        """
        Constructor.
        """
        self._canID = msg_id
        self._name = msg_name
        self._dlc = msg_dlc
        self._txNode = msg_tx

    def __iter__(self):
        """
        Defined to make the object iterable.
        """
        self._iter_index = 0
        return self

    def __next__(self):
        """
        Defines the next CANSignal object to be returned in an iteration.
        """
        if self._iter_index == len(self._signals):
            raise StopIteration
        self._iter_index += 1
        return self._signals[self._iter_index]

    def AddSignal(self, signal):
        """
        Takes a CANSignal object and adds it to the list of signals.
        """
        self._signals += [signal]
        return self

    def Signals(self):
        """
        Gets the signals in a CANMessage object.
        """
        return self._signals

    def SetComment(self, comment_str):
        """
        Sets the Comment property for the CANMessage.
        """
        self._comment = comment_str

        return self

    def CANID(self):
        """
        Gets the message's CAN ID.
        """
        return self._canID

    def AddValue(self, value_tuple):
        """
        Adds a enumerated value mapping to the appropriate signal.
        """
        for signal in self:
            if signal.Name() == value_tuple[0]:
                signal.SetValues(value_tuple[2])
                break
        return self

    def AddAttribute(self, attr_tuple):
        """
        Adds an attribute to the message.
        """
        self._attributes.append(attr_tuple)
        return self

    def ResetSignals(self):
        """
        Flushes all the signals from the CANMessage object.
        """
        self._signals = []
        return self

    def ResetAttributes(self):
        """
        Flushes all the attributes from the CANMessage object.
        """
        self._attributes = []
        return self


class CANSignal:
    """
    Contains information describing a signal in a CAN message.
    """
    _name = ""
    _type = None
    _format = None
    # _mode = None # have to figure out why I wrote this one down...
    _startbit = 0
    _length = 0
    _offset = 0
    _factor = 1
    _minVal = 0
    _maxVal = 0
    _units = ""
    _values = list()

    def __init__(self, name, sigtype, sigformat, startbit, length, offset, factor,
                 minVal, maxVal, unit):
        """
        Constructor.
        """
        self._name = name
        self._type = sigtype
        self._format = sigformat
        self._startbit = startbit
        self._length = length
        self._offset = offset
        self._factor = factor
        self._minVal = minVal
        self._maxVal = maxVal
        self._units = unit

    def Name(self):
        """
        Gets the name of the CANSignal.
        """
        return self._name

    def SetValues(self, values_lst):
        """
        Sets the enumerated value map for the signal's data.
        """
        self._values = values_lst
        return self


class Format(Enum):
    """
    Enumeration for the endianness of the signals.
    """
    Motorola = 0  # Big-Endian
    Intel = 1  # Little-Endian


class Type(Enum):
    """
    Enumeration for whether a signal is signed or unsigned.
    """

    Unsigned = '-'
    Signed = '+'


class IDType(Enum):
    """
    Enumeration containing whether a CAN ID is using an extended ID or standard
    ID.
    """

    Standard = 0
    Extended = 1


def valueLineSplit(line):
    """
    Custom split function for splitting up the components of a value line.

    Could not use normal String.split(' ') due to spaces in some of the value
    name strings.
    """
    components = list()
    part = ""
    in_quotes = False
    for ch in line:
        if ch == ' ' and not in_quotes:
            components.append(part)
            part = ""
        elif ch == '"' and not in_quotes:
            in_quotes = True
        elif ch == '"' and in_quotes:
            in_quotes = False
        else:
            part += ch
    return components


def checkMessageMemoryAlignment(message):
    """
    Examines a CANMessage object and checks that signals in the message are
    properly arranged so as to minimize padding in the struct bitfield. If a
    message cannot fit into the DLC that has been defined for it, this function
    will stop header file generation and raise an error.
    """
    pass


def main():
    """
    Opens a DBC file and parses it into a CANDatabase object and uses the
    information to generate a C header file for the Network Manager
    application.
    """
    file = "test_EVT_CAN.dbc"
    candb = CANDatabase(file)
    candb.Load()
    input()

if __name__ == "__main__":
    main()
