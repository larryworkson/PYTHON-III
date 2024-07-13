import rpa as r
import pyautogui as p

#robo abre camera do computador e captura tela salvando uma imagem no desktop.
p.hotkey('win', 'r')
p.typewrite('cmd')
p.press('enter')
p.sleep(1)
p.typewrite('start microsoft.windows.camera:')
p.sleep(3)
ps = p.screenshot()
ps.save('C:/Users/studi/OneDrive/Área de Trabalho/telacapturada.png')
valor = p.getActiveWindow()
valor.close()

#   python robot01.py