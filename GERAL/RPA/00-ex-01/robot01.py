import pyautogui as p

#robo abre camera do computador e captura tela salvando uma imagem no desktop.
p.hotkey('win', 'r')
p.typewrite('cmd')
p.press('enter')
p.sleep(1)
p.typewrite('start microsoft.windows.camera:')
p.press('enter')
p.sleep(3)
ps = p.screenshot()
ps.save('C:/Users/studi/OneDrive/Área de Trabalho/telacapturada.png')
jn1 = p.getActiveWindow()
jn1.close()

#   python robot01.py