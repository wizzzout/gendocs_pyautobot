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

# MAIN
def waiting():
  itr = 0

  while itr < len(screens):
    try:
      pyautogui.locateOnScreen(screens[itr]['screen'], confidence=screens[itr]['conf'])
      print('I see image', screens[itr]['name'])
      return screens[itr]['name']
    except pyautogui.ImageNotFoundException:
      print('I dont see image')
      itr += 1
      if itr == len(screens):
        itr = 0

# MAIN 
def main(arr):
  pyautogui.click(730, 90)
  itr = len(arr)

  for i in range(itr):
    action = waiting()

    if action == 'AllList#1' or action == 'AllList#2':
      print('Вижу общий список: ' 'Нажимаю F9')
      # Копия документа
      pyautogui.hotkey('F9')
      time.sleep(0.3)
      # Ожидание действия
      action = waiting()
      if action == 'OneDocFilling':
        print('Вижу документ: ' 'Заполняю поля, нажимаю ОК')
        # Первая дата
        pyautogui.click(826, 290)
        keyboard.write(data[i][1])
        # Вторая дата
        pyautogui.click(826, 360)
        keyboard.write(data[i][1])
        # Номер счет-фактуры
        pyautogui.click(656, 360, button='right')
        pyautogui.click(730, 570)
        keyboard.write(data[i][2])
        # Сумма
        pyautogui.doubleClick(695, 638)
        keyboard.write(data[i][0])
        # Ок
        time.sleep(0.2)
        pyautogui.click(200, 1350)

        # Ожидание действия
        action = waiting()
        if action == 'OneDocCarryOut':
          # Да
          pyautogui.click(580, 835)

          # Ожидание действия
          action = waiting()
          if action == 'OneDocClose':
            # Закрыть
            pyautogui.click(445, 290)
          else:
            print('Ошибка при закрытии')
            print('Ошибка удалите часть масима сначала', i)
            break
        else:
          print('Ошибка при ок')
          print('Ошибка удалите часть масима сначала', i)
          break
      else:
        print('Ошибка при заполнении')
        print('Ошибка удалите часть масима сначала', i)
        break
    else:
      print('Ошибка удалите часть масима сначала', i)
      break

#main(data)

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
    moveEnter()

    keyboard.press_and_release('shift + alt')
    pyautogui.doubleClick(580, 240)
    moveCopy()
    dataMoves['current'] = pyperclip.paste()
    print(dataMoves['current'])

    pyautogui.doubleClick(580, 300)
    moveChangeString()
    moveCopy()
    dataNums.append(pyperclip.paste())
    print(pyperclip.paste())
    keyboard.press_and_release('shift + alt')

    pyautogui.click(1270, 105)
    moveTab()
    moveEnter()
    moveArrowDown()
  print(dataNums)

# Test Script
moveScript()