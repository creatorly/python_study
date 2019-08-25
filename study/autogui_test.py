import pyautogui

location = pyautogui.locateOnScreen(image='test.png')
print(location)
try:
    x, y = pyautogui.center(location)
    print(x, y)
except Exception as err:
    print(err)

location = pyautogui.locateAllOnScreen(image='test.png')
try:
    for i in location:
        x, y = pyautogui.center(i)
        print(x, y)
except Exception as err:
    print(err)

print(pyautogui.size())
print(pyautogui.position())

pyautogui.moveTo(x, y, duration=3)
pyautogui.click()

