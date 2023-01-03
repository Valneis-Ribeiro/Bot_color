import pyautogui as pt
import time
import subprocess
from Gix import Gix
from AssistenteAudio import AssistenteVoz
from AssistentePedidos import BotPedidosBaixa

class IquineBBF:
    def __init__(self):
        pass

    def localizarElemento(self,img):
        while not pt.locateOnScreen(img, grayscale=True,confidence=0.90):
            time.sleep(1)
        encontrou = pt.locateOnScreen(img, grayscale=True, confidence=0.90)
        # pt.alert('Acabeide encontrar a imagem solicitada')
        return encontrou


    def localizarElemento_True(self,img):
        while pt.locateOnScreen(img, grayscale=True,confidence=0.90):
            time.sleep(1)
        pass


    def login(self):
        # Inicializar BBF
        subprocess.Popen([r'C:\BBFCoresTIRevenda\BBFCoresTI'])
        #usuario
        encontrou = self.localizarElemento(
        r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\usuario.png')
        pt.write('super')
        pt.press('enter')
        #usuario
        encontrou = self.localizarElemento(
        r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\senha.png')
        pt.write('iquine')
        # código de usuário
        encontrou =self.localizarElemento(r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\logar.png')
        pt.click(encontrou)
        time.sleep(2)
        pt.write('1')
        pt.press('enter')
        pt.press('enter')
        pt.press('enter')


    def EncerraAutomacao(self,x=1023, y=0):
        return x, y


    def pigVirtual(self):

        gix = Gix().PreVendas_Tintas()

        if gix == 'lista_vazia':

            pt.alert('PIGMENTADOR VIRTUAL:\n\n\n'
                     'Não há tintas para fazer ou essa cor não é referencia IQUINE\n\n'
                      'Deseja realizar uma nova consulta ?')

        else:

            pt.alert('ATIVAR: PIGMENTADOR VIRTUAL ::::::::::::::::::::::::::::')

            # AssistenteVoz(r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\Speak\ativado.txt')
            # time.sleep(2)
            #
            # # Voz de comando
            # AssistenteVoz(r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\Speak\pigmentos.txt')
            #
            # time.sleep(2)
            #
            # pt.alert('Tendo verificado, click em OK.')
            #
            # time.sleep(2)
            #
            # # Voz de comando
            # AssistenteVoz(r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\Speak\aguarde.txt')

            time.sleep(2)

            # Dados tratados extraidos do GIX Navegador ( Dados Principais)
            time.sleep(3)
            codigo = gix[0]
            acabamento = gix[1]
            embalagem = gix[2]
            quantidade = gix[3]
            quantidade = str(quantidade).replace(',00', '')
            quantidade = int(quantidade)

            # time.sleep(2)
            #
            # # # Voz de comando
            # # AssistenteVoz(r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\Speak\verificando.txt')
            #
            # time.sleep(2)
            #
            # # # Voz de comando
            # # AssistenteVoz(r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\Speak\momento.txt')

            time.sleep(4)

            # Modulo de dosagem
            encontrou = self.localizarElemento(
            r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\balde_tinta.png')
            pt.doubleClick(encontrou)

            time.sleep(2)

            # # Voz de comando
            # AssistenteVoz(r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\Speak\dados_exportados.txt')

            time.sleep(2)

            #Código/Cor
            self.localizarElemento(r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\codigo.png')
            pt.write(str(codigo))
            pt.press('enter')
            pt.click(x=496, y=289)

            # acabamento
            if acabamento == 'LIMP':
                pt.click(x=496, y=289)
                for i in range(22):
                    pt.vscroll(-1)
                time.sleep(2)
                encontrou = self.localizarElemento(
                r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\limpa_facil.png')
                pt.doubleClick(encontrou)

            elif acabamento == 'BRI':

                # acabamento
                pt.click(x=496, y=289)
                for i in range(12):
                    pt.vscroll(-1)
                time.sleep(2)
                encontrou = self.localizarElemento(
                    r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\brilho_seda.png')
                pt.doubleClick(encontrou)


            elif acabamento == 'PROT':

                # acabamento
                pt.click(x=496, y=289)
                for i in range(20):
                    pt.vscroll(-1)
                time.sleep(2)
                encontrou = self.localizarElemento(
                    r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\prot.png')
                pt.doubleClick(encontrou)


            elif acabamento == 'FOSC':

                # acabamento
                pt.click(x=496, y=289)
                for i in range(20):
                    pt.vscroll(-1)
                time.sleep(2)
                encontrou = self.localizarElemento(
                    r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\fosco.png')
                pt.doubleClick(encontrou)


            elif acabamento == 'DEL' or acabamento == 'DIAPISO':

                # acabamento
                pt.click(x=496, y=289)
                for i in range(20):
                    pt.vscroll(-1)
                time.sleep(2)
                encontrou = self.localizarElemento(
                    r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\delanil.png')
                pt.doubleClick(encontrou)

            # embalagem
            encontrou = self.localizarElemento(
                r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\embalagem.png')
            pt.click(encontrou)

            # Analisando o tamanho da embalagem
            # Embalagem
            if embalagem == '16L':
                encontrou = self.localizarElemento(
                    r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\embalagem.png')
                pt.click(encontrou)

                time.sleep(3)

                # correção de bug
                pt.click(x=703, y=412)

                # tipo volume
                encontrou = self.localizarElemento(
                    r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\latao.png')
                time.sleep(1)
                pt.click(encontrou)


                # Quantidade
                encontrou = self.localizarElemento(
                    r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\quantidade.png')
                pt.click(encontrou)
                pt.write(str(quantidade))


            if embalagem == '3,200L':

                # Embalagem
                encontrou = self.localizarElemento(
                    r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\embalagem.png')
                time.sleep(3)
                pt.click(encontrou)


                time.sleep(3)

                # correção de bug
                pt.click(x=703, y=412)

                # tipo volume
                encontrou = self.localizarElemento(
                    r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\galao.png')
                time.sleep(2)
                pt.click(encontrou)

                # Quantidade
                encontrou = self.localizarElemento(
                    r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\quantidade.png')
                pt.click(encontrou)
                pt.write(str(quantidade))


            time.sleep(1)

            # Opção produção
            pt.click(x=708, y=453)

            #dosar
            encontrou = self.localizarElemento(
                r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\dosar.png')
            pt.click(encontrou)
            time.sleep(1)
            pt.write('1')
            pt.press('enter')

            # Avaliando se a quantidade se é  maior que 1

            dsg_executadas = []

            quantidade = int(quantidade)
            if quantidade > 1:
                 while sum(dsg_executadas) <= quantidade:
                    pt.alert('Cuidado!! Verifique antes de  pertar (OK), cor, código, acabamento e volume\n'
                             'observando se  estão em conformidade com a Pré - Venda e GIX WEB.'
                             'Caso esteja em conformidade aperte em OK.')

                    # executar dosagem
                    encontrou = self.localizarElemento(
                        r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\confirmar_dsg1.png')
                    pt.click(encontrou)


                    # metodo para avança acaso tenha terminado
                    encontrou = self.localizarElemento_True(
                        r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\dosando.png')

                    # proxima embalagem
                    encontrou = self.localizarElemento(
                        r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\foi_dosado.png')
                    pt.click(encontrou)

                    dsg_executadas.append(1)

                    if dsg_executadas == quantidade:

                        # Mensagem de finalização
                        pt.alert('Produção concluída com sucesso')

                        # final de dosagem
                        finalProcesso = self.localizarElemento(
                            r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\fim_dsg.png')
                        pt.click(finalProcesso)

                        # inicializar produção
                        pt.click(x=888, y=74)
                        time.sleep(10)
                        pt.click(x=888, y=74)

                        #BotPedidosBaixa()

            if quantidade == 1:
                    pt.alert('Cuidado!! Verifique antes de  pertar (OK), cor, código, acabamento e volume\n'
                             'observando se  estão em conformidade com a Pré - Venda e GIX WEB.'
                             'Caso esteja em conformidade aperte em OK.')

                    # executar dosagem
                    encontrou = self.localizarElemento(
                        r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\confirmar_dsg1.png')
                    pt.click(encontrou)

                    time.sleep(2)

                    # proxima embalagem
                    encontrou = self.localizarElemento(
                        r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\foi_dosado.png')
                    pt.click(encontrou)

                    time.sleep(2)

                    # final de dosagem
                    finalProcesso = self.localizarElemento(
                        r'C:\Users\iquine.pc\Desktop\PIGMENTADOR_VIRTUAL\img_Iquine\fim_dsg.png')
                    pt.click(finalProcesso)

                    # inicializar produção
                    pt.click(x=888, y=74)
                    time.sleep(10)
                    pt.click(x=888, y=74)

                    #BotPedidosBaixa()








