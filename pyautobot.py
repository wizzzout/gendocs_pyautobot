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
from movescript import *

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

#copy = pyautogui.locateOnScreen('./screenshots/btn_copy.png', confidence=0.96)


# MAIN 
def main(arr):
  pyautogui.click(1150, 200)
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
        string_change = pyautogui.locateOnScreen('./screenshots/btn_change_string.png', confidence=0.96)
        string_save = pyautogui.locateOnScreen('./screenshots/btn_save_string.png', confidence=0.96)
        print('Вижу документ: ' 'Заполняю поля, нажимаю ОК')
        # Первая дата
        pyautogui.click(690, 280)
        keyboard.write(data[i][1])
        # Вторая дата
        pyautogui.click(690, 340)
        keyboard.write(data[i][1])
        # Номер счет-фактуры
        pyautogui.click(550, 340, button='right')
        pyautogui.click(600, 512)
        keyboard.write(data[i][2])
        # Сумма
        pyautogui.click(600, 575)
        pyautogui.click(string_change)
        keyboard.write(data[i][0])
        pyautogui.click(string_save)
        
        # Ок
        time.sleep(0.2)
        pyautogui.click(170, 1360)
        time.sleep(0.3)

        # Ожидание действия
        action = waiting()
        if action == 'OneDocCarryOut':
          # Да
          pyautogui.click(590, 820)

          # Ожидание действия
          action = waiting()
          if action == 'OneDocClose':
            # Закрыть
            pyautogui.click(370, 250)
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

main(data)