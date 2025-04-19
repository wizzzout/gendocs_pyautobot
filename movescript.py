# LIBS
import pyautogui
import keyboard
import time
import pyperclip

# Screen models
from screens import get_screen_data
screens = get_screen_data()

# DATA
from autodata import get_data
data = get_data()

# Moves
from moves import *

dataMoves = {
  'start': 0,
  'end': 0,
  'current': 0,
  'to': 0, 
}

dataNums = []

def moveScript():
  itr = 0
  pyautogui.click(580, 70)

  moveEnter()
  pyautogui.doubleClick(580, 240)
  moveCopy()
  dataMoves['start'] = pyperclip.paste()

  moveEsc()

  movePageDown()
  movePageDown()
  movePageDown()
  movePageDown()

  moveEnter()
  pyautogui.doubleClick(580, 240)
  moveCopy()
  dataMoves['end'] = pyperclip.paste()

  moveEsc()

  movePageUp()
  movePageUp()
  movePageUp()
  movePageUp()

  itr = int(dataMoves['end']) - int(dataMoves['start']) + 1
  print(itr)

  for i in range(itr):

    dataNums.append({
      'nameCompany': 'none',
      'numDoc': 'none',    
      'num1C': 'none',
    })

    #Вход в документ
    moveEnter()

    pyautogui.doubleClick(580, 240)
    moveCopy()
    dataMoves['current'] = pyperclip.paste()
    dataNums[i]['num1C'] = pyperclip.paste()
    if (i > 2):
      if (dataNums[-2]['num1C'] == pyperclip.paste()):
        break
    #log
    print(dataMoves['current'])

    #Переключение языка
    keyboard.press_and_release('shift + alt')

    pyautogui.doubleClick(580, 300)
    moveChangeString()
    moveCopy()
    dataNums[i]['numDoc'] = pyperclip.paste()

    #log
    print(pyperclip.paste())

    #Переключение языка
    keyboard.press_and_release('shift + alt')

    #Выход из документа
    pyautogui.click(1270, 105)
    moveTab()
    moveEnter()
    moveArrowDown()
  #log
  print(dataNums)