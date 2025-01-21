# LIBS
import pyautogui

def changeLanguage():
  pyautogui.hotkey('shift', 'ctrl')

def moveCopy():
  pyautogui.hotkey('ctrl', 'c')
def movePaste():
  pyautogui.hotkey('ctrl', 'v')
def moveTab():
  pyautogui.hotkey('tab')


def moveArrowUp():
  pyautogui.hotkey('up')
def moveArrowDown():
  pyautogui.hotkey('down')

def movePageUp():
  pyautogui.hotkey('pageup')
def movePageDown():
  pyautogui.hotkey('pagedown')

# Exit Document
def moveEsc():
  pyautogui.hotkey('escape')
# Enter Document
def moveEnter():
  pyautogui.hotkey('enter')
# Copy Document
def moveF9():
  pyautogui.hotkey('F9')
# Change String
def moveChangeString():
  pyautogui.hotkey('shift', 'enter')


def moveCheck():
  pyautogui.click()
