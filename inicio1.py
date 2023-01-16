import pyautogui
import time 
import pyperclip


#time.sleep(4)
#print(pyautogui.position())
senha = ('986532')
pyautogui.click(x=109, y=227,clicks=2)
time.sleep(1)
pyautogui.click(x=487, y=198,duration=2,clicks=2)
time.sleep(1)
pyautogui.click(x=516,y=442)
time.sleep(1)
pyautogui.write("aless")
pyautogui.press("tab")
pyautogui.write("986532")
time.sleep(1)
pyautogui.click(x=420, y=444)
pyautogui.write("aless")
pyautogui.press("tab")
pyautogui.write("986532")
pyautogui.click(x=420, y=444,duration=1)

# abrir arquivo de texto 
with open ('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(x=246,y=368,duration=0.5)
        pyautogui.write(produto)
        pyautogui.click(x=256,y=398,duration=0.5)
        pyautogui.write(quantidade)
        pyautogui.click(x=246,y=425,duration=0.5)
        pyautogui.write(preco)
        pyautogui.click(x=144,y=581)
        time.sleep(0.5)