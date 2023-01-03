from Iquine import IquineBBF as BBF
bbf = BBF()
import pyautogui as pt


encerraPrograma = bbf.EncerraAutomacao()

while True:
    if pt.position() == encerraPrograma:
        break
    # Pigmentador Virtual
    bbf.pigVirtual()




