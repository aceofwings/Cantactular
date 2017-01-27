=================
Object Dictionary
=================
The Object dictionary is essential for mapping communication between two CAN-OPEN devices. Each device may have its own version or revision of an object dictionary but none the less it is a properly formatted file following a set of simple rules.

Things to know
 * Object dictionary files end in extension **.eds**
 * Files are similar to a glorified ini files

Lets look at an entry in the motor-controller Object Dictionary:
::

    [2220]
    **1.** ParameterName=Throttle Input Voltage
    **2.** ObjectType=7
    **3.** DataType=3
    **4.** AccessType=rww
    **5.** LowLimit=-32768
    **6.** HighLimit=32767
    **7.** PDOMapping=1
    **8.** ObjFlags=0x1
    ;SEVCONFIELD OBJECT_VERSION=1
    ;SEVCONFIELD SCALING=0.00390625
    ;SEVCONFIELD UNITS=V
    ;SEVCONFIELD OBJECT=ANALOGUE_SIGNAL_IN
    ;SEVCONFIELD SECTION=TractionAI
    ;SEVCONFIELD MASTER=TRUE
    ;SEVCONFIELD CATEGORY=MONITORING

The first thing an entry has is a header. The header will always be in the
"[]". In this case [2220] and represents the **index**


 1.Parameter name is simply the name of the object.

 2.Object Type -an integer which points to the object type.

 3.DataType - an integer representing a type of data eg. String,Int,Short

 4.AccessType - denotes the permissions and actions of this object Read,Write,Write)

 5.LowLimit - the max  you can set that object

 6.HighLimit - the lowest value you can set that object

 7.Unknown

 8.Unkown


There are addition Sevcon fields, commented for no reason, that help describe
the object more.

Index
------
An index is simply a hex number referencing an object and is how we do our look
ups similar to a database.
There are always defined as a simple hex number within brackets eg.[2220] and
have a data type of 7(Var)

SubIndex
---------
A subindex is also a hex number but references the parent index and  has a
subindex ID appended to it. eg. [2220sub0], [2220sub1].
In the motor Controller they always have a type 9(Array)

Object Types
------------
Types are represented by integers known as codes and describe the objects name
and characteristics

The ones that are concerned in our motor-controller object dictionary are
 * 7 = Var   an object that is not a considered a subindex or a standalone object
 * 9 = Record   an object associated with an index

Data Types
-----------
 Types are represented by integers and describe the data type area.
 Several of them are:

  * 1 = Boolean
  * 2 = Integer8 ...........(Byte)
  * 3 = Integer16......... (Short)
  * 4 = Intger32........... (Int)
  * 5 = Unsigned8....... (unsigned Byte)
  * 6 = Unsigned16...... (unsigned Short)
  * 7 = Unsigned32...... (unsigned Int)
