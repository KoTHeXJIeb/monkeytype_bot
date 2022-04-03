
import pyscreenshot
import pyautogui
from PIL import Image
from pytesseract import pytesseract
import time
import webbrowser

webbrowser.open('https://monkeytype.com/')
time.sleep(5)
image = pyscreenshot.grab(bbox=(450, 500, 1450, 650)) # X1,Y1,X2,Y2
image.save("words.jpg")

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(Image.open('./words.jpg'))
list(text).insert(0, ' ')
print(text[:-1])
for i in text:
    if i == '\n': pyautogui.press('enter')
    pyautogui.write(i, interval=0.1)

