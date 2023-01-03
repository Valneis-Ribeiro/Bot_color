import pyautogui as pt
import time
class BotPedidosBaixa:

    def __ini__(self):
        pass

    def localizarElemento(self,img):
        while not pt.locateOnScreen(img, grayscale=True,confidence=0.90):
            time.sleep(1)
        encontrou = pt.locateOnScreen(img, grayscale=True, confidence=0.90)
        # pt.alert('Acabeide encontrar a imagem solicitada')
        return encontrou

    def BaixarPedidos(self):

        # Gix Web
        encontrou = self.localizarElemento(
        r'C:\Users\pigmentacao.centro.CDC\Desktop\PIGMENTADOR_VIRTUAL\img_assistentePedidos\gix_web.png')
        pt.click(encontrou)

        # ponto de referncia
        pt.click(x=736, y=291)

        #Iniciar
        encontrou = self.localizarElemento(
        r'C:\Users\pigmentacao.centro.CDC\Desktop\PIGMENTADOR_VIRTUAL\img_assistentePedidos\iniciar.png')
        pt.click(encontrou)

        #Confirmar inicio
        encontrou = self.localizarElemento(
        r'C:\Users\pigmentacao.centro.CDC\Desktop\PIGMENTADOR_VIRTUAL\img_assistentePedidos\confirmar_inicio.png')
        pt.click(encontrou)

        # #Opções
        # encontrou = self.localizarElemento(
        # r'C:\Users\pigmentacao.centro.CDC\Desktop\PIGMENTADOR_VIRTUAL\img_assistentePedidos\opcoes.png')
        # pt.click(encontrou)

        # #Emitir Etiqueta
        # encontrou = self.localizarElemento(
        # r'C:\Users\pigmentacao.centro.CDC\Desktop\PIGMENTADOR_VIRTUAL\img_assistentePedidos\emitir_etiqueta.png')
        # pt.click(encontrou)

        # ponto de referencia
        pt.click(x=736, y=291)

        #Dar baixa
        encontrou = self.localizarElemento(
        r'C:\Users\pigmentacao.centro.CDC\Desktop\PIGMENTADOR_VIRTUAL\img_assistentePedidos\baixar.png')
        pt.click(encontrou)

        #confirmar baixa
        encontrou = self.localizarElemento(
        r'C:\Users\pigmentacao.centro.CDC\Desktop\PIGMENTADOR_VIRTUAL\img_assistentePedidos\confirmar_baixa.png')
        pt.click(encontrou)


