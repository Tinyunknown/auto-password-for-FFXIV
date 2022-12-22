#imports pyautogui for use
import pyautogui

#sets up variables for your password
password = "your password"

#finds where the password box is and stores it in a variable
if pyautogui.locateCenterOnScreen('password.png') == pyautogui.ImageNotFoundException():
	x, y = pyautogui.locateCenterOnScreen('password2.png')
else:
	x, y = pyautogui.locateCenterOnScreen('password.png')

#moves the mouse to the password box, clicks it, and enters the password
pyautogui.moveTo(x, y)
pyautogui.click()
pyautogui.write(password)

#gets the coords for the login button, then clicks it
x, y = pyautogui.locateCenterOnScreen('login.png')
pyautogui.click(x, y)
