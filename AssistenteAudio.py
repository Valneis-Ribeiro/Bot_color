import time
import pyttsx3  # pip instal pyttsx3


def AssistenteVoz(texto):

        arquivo = open(texto)
        texto_arq = arquivo.read()

        speaker = pyttsx3.init()  # inicia serviço biblioteca
        voices = speaker.getProperty('voices')  # metodo de voz

        # ver as vozes instaladas na maquina
        # for voice in voices:
        #         print(voice, voice.id)  # traz os idiomas de voz instalados em sua maquina

        speaker.setProperty('voice', voices[0].id)  # define a voz padrao, no meu caso o portugues era o[2] (iniciando do zero)
        rate = speaker.getProperty('rate')
        speaker.setProperty('rate', rate - 25)  # muda velocidade da leitura, quando menor mais lento

        print(texto_arq)  # escreve o texto na tela
        speaker.say(texto_arq)  # define o texto que será lido
        speaker.runAndWait()  # le o texto
        arquivo.close()

# base = '16L'
#
# if base == '16L':
#         AssistenteVoz('Coloque a badeja no primeiro nível da maquina')
#         AssistenteVoz('Coloque a badeja no primeiro nível da maquina')