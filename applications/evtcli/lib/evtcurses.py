import curses
from threading import Lock
import time
class ScreenObject(object):
    """
    An object with a location on the screen denoted by (x,y)
    Contains a text string providing context to the data being presented
    Controllers then update the data attribute to affectively change what is being displayed on the screen

    """
    x = None
    y = None
    colorPair = 0
    text = "None"
    _data = 0
    @property
    def data(self):
        """
        returns:
            current data object stored
        """
        return str(self._data)

    @data.setter
    def data(self,value):
        """
        Must be an object that can be string translatable. Make sure you add a to_str method
        if you are setting objects in the data field

        sets the current data.

        """
        self._data = value

    def __init__(self,x,y,text):
        self.x = x
        self.y = y
        self.text = text


screenObjectsLock = Lock()
"""Global screen object state shared between controllers"""
screenObjects = []
ORANGE = 209
DARK = 17



def appendToScreenObjects(screenObject):
    """
    thread safe way of adding objects for curses then to update the screen with
    """
    with screenObjectsLock:
        screenObjects.append(screenObject)

def startCurses(running):
    """
    sets up the terminal with the standard init sequence. On deinit the function
    is responsible for restoring the terminal to its normal state
    """
    curses.wrapper(text_screen, running)

def text_screen(stdscr,running):
    """
    layouts and updates all screenobjects on the terminal

    paramters :
        running - Application or Engines state
        stdscr - the display to write too.
    """
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    while not running.isSet():
        stdscr.clear()
        with screenObjectsLock:
            for so in screenObjects:
                stdscr.addstr(so.y,so.x, so.text + so.data,curses.color_pair(so.colorPair))
        stdscr.refresh()
        time.sleep(.1)
