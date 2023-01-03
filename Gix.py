import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui as pt

class Gix:

    def __init__(self):
        pass
    def PreVendas_Tintas(self):

        options = Options()
        options.add_argument("--headless")
        eped_gix = webdriver.Chrome(options=options)
        eped_gix.get('http://192.168.100.3:30002/logistica/')
        time.sleep(1)
        usuario = eped_gix.find_element(By.TAG_NAME,'input')
        usuario.send_keys('pigmentador')
        senha = eped_gix.find_element(By.ID,'mat-input-1')
        senha.send_keys('pig4050')
        senha.submit()
        time.sleep(6)

        lista_ordem = eped_gix.find_element(By.CLASS_NAME,value='mat-table').text
        time.sleep(5)

        trat_dados = lista_ordem.split()
        trat_dados = trat_dados[:39]

        trat_dados = trat_dados[30:]
        time.sleep(2)

        if trat_dados:

        #     # posicao_suvinil = trat_dados.index('SUVINIL')
        #     # # time.sleep(2)
        #     # # # return trat_dados,posicao_suvinil
        #     # #
            posicao_iquine = trat_dados.index('IQUINE')
        #
            time.sleep(2)
        #     # #
        #     # posicao_coral = trat_dados.index('CORAL')
        #     #
        #     # # #
        #     # # #
        #     # # # #
            # # # # time.sleep(2)
            # # # #
            if posicao_iquine:
                # ACABAMENTO COM 3 PALAVRAS E COR COM 3 PALAVRAS
                if trat_dados[0] == 'DEL' and trat_dados[1] == 'REN' and trat_dados[2] == 'MT' and posicao_iquine == 8:
                    codigo = trat_dados[3]
                    acabamento = trat_dados[0]
                    embalagem = trat_dados[9]
                    quantidade = trat_dados[10]

                    lista_def = [codigo, acabamento, embalagem, quantidade]

                    return lista_def

                # ACABAMENTO COM 3 PALAVRAS E COR COM 2 PALAVRAS
                if trat_dados[0] == 'DEL' and trat_dados[1] == 'REN' and trat_dados[2] == 'MT' and posicao_iquine == 7:
                    codigo = trat_dados[3]
                    acabamento = trat_dados[0]
                    embalagem = trat_dados[7]
                    quantidade = trat_dados[8]

                    lista_def = [codigo, acabamento, embalagem, quantidade]

                    return lista_def

                # ACABAMENTO COM 3 PALAVRAS E COR COM 1 PALAVRA
                if trat_dados[0] == 'DEL' and trat_dados[1] == 'REN' and trat_dados[2] == 'MT' and posicao_iquine == 6:
                    codigo = trat_dados[3]
                    acabamento = trat_dados[0]
                    embalagem = trat_dados[7]
                    quantidade = trat_dados[8]

                    lista_def = [codigo, acabamento, embalagem, quantidade]

                    return lista_def
                #________________________________________________________________________________________
                #Altera para loja japiim
                #ACABAMENTO COM 2 PALAVRAS E COR COM 1 PALAVRAS
                if trat_dados[0] == 'LIMP' and trat_dados[1] == 'FACIL' and posicao_iquine == 5 \
                        or trat_dados[0] == 'FOSC' and trat_dados[1] == 'DURA' and posicao_iquine == 5 or \
                        trat_dados[0] == 'PROT' and trat_dados[1] == 'ANTIBAC' and posicao_iquine  == 5 or \
                        trat_dados[0] == 'BRI' and trat_dados[1] == 'SEDA' and posicao_iquine  == 5:
                    time.sleep(3)
                    codigo = trat_dados[2]
                    acabamento = trat_dados[0]
                    embalagem = trat_dados[6]
                    quantidade = trat_dados[7]

                    lista_def = [codigo, acabamento, embalagem, quantidade]
                    time.sleep(2)
                    return lista_def
                #
                # ACABAMENTO COM 2 PALAVRAS E COR COM 2 PALAVRAS
                if trat_dados[0] == 'LIMP' and trat_dados[1] == 'FACIL' and posicao_iquine == 6 \
                        or trat_dados[0] == 'FOSC' and trat_dados[1] == 'FOSC' == 6 or \
                        trat_dados[0] == 'PROT' and trat_dados[1] == 'ANTIBAC' == 6 or \
                        trat_dados[0] == 'BRI' and trat_dados[1] == 'SEDA' == 6:
                    codigo = trat_dados[2]
                    acabamento = trat_dados[0]
                    embalagem = trat_dados[7]
                    quantidade = trat_dados[8]
                    time.sleep(2)
                    lista_def = [codigo, acabamento, embalagem, quantidade]

                    return lista_def

                # ACABAMENTO COM 2 PALAVRAS E COR COM 3 PALAVRAS
                if trat_dados[0] == 'LIMP' and trat_dados[1] == 'FACIL' and posicao_iquine == 7 \
                        or trat_dados[0] == 'FOSC' and trat_dados[1] == 'FOSC' == 7 or \
                        trat_dados[0] == 'PROT' and trat_dados[1] == 'ANTIBAC' == 7 or \
                        trat_dados[0] == 'BRI' and trat_dados[1] == 'SEDA' == 7:
                    pt.alert('Abamento com 2 palavras E cor com 3 palavra')
                    codigo = trat_dados[2]
                    acabamento = trat_dados[0]
                    embalagem = trat_dados[8]
                    quantidade = trat_dados[9]
                    time.sleep(2)
                    lista_def = [codigo, acabamento, embalagem, quantidade]

                    return lista_def

            # if posicao_suvinil:
            #     #ACABAMENTO COM 3 PALAVRAS E COR COM 3 PALAVRAS
            #     if trat_dados[0] == 'DEL' and trat_dados[1] == 'REN' and trat_dados[2] == 'MT' and posicao_suvinil == 8:
            #         codigo = trat_dados[3]
            #         acabamento = trat_dados[0]
            #         embalagem = trat_dados[9]
            #         quantidade = trat_dados[10]
            #         pt.alert('Abamento com 3 palavras E cor com 3 palavra')
            #         lista_def = [codigo, acabamento, embalagem, quantidade]
            #
            #         return lista_def
            #
            #     # ACABAMENTO COM 3 PALAVRAS E COR COM 2 PALAVRAS
            #     if trat_dados[0] == 'DEL' and trat_dados[1] == 'REN' and trat_dados[2] == 'MT' and posicao_suvinil == 7:
            #         codigo = trat_dados[3]
            #         acabamento = trat_dados[0]
            #         embalagem = trat_dados[7]
            #         quantidade = trat_dados[8]
            #         pt.alert('Abamento com 3 palavras E cor com 2 palavra')
            #         lista_def = [codigo, acabamento, embalagem, quantidade]
            #
            #         return lista_def
            #
            #     # ACABAMENTO COM 3 PALAVRAS E COR COM 1 PALAVRA
            #     if trat_dados[0] == 'DEL' and trat_dados[1] == 'REN' and trat_dados[2] == 'MT' and posicao_suvinil == 6:
            #         codigo = trat_dados[3]
            #         acabamento = trat_dados[0]
            #         embalagem = trat_dados[7]
            #         quantidade = trat_dados[8]
            #         pt.alert('Abamento com 3 palavras E cor com 1 palavra')
            #         lista_def = [codigo, acabamento, embalagem, quantidade]
            #
            #         return lista_def
            #     #________________________________________________________________________________________
            #     #ACABAMENTO COM 2 PALAVRAS E COR COM 1 PALAVRAS
            #     if trat_dados[0] == 'LIMP' and trat_dados[1] == 'FACIL' and posicao_suvinil == 5 \
            #             or trat_dados[0] == 'FOSC' and trat_dados[1] == 'DURA' and posicao_suvinil == 5 or \
            #             trat_dados[0] == 'PROT' and trat_dados[1] == 'ANTIBAC' and posicao_suvinil  == 5 or \
            #             trat_dados[0] == 'BRI' and trat_dados[1] == 'SEDA' and posicao_suvinil  == 5:
            #         time.sleep(3)
            #         codigo = trat_dados[2]
            #         acabamento = trat_dados[0]
            #         embalagem = trat_dados[6]
            #         quantidade = trat_dados[7]
            #
            #         lista_def = [codigo, acabamento, embalagem, quantidade]
            #         time.sleep(2)
            #         return lista_def
            #     #
            #     # ACABAMENTO COM 2 PALAVRAS E COR COM 2 PALAVRAS
            #     if trat_dados[0] == 'LIMP' and trat_dados[1] == 'FACIL' and posicao_suvinil == 6 \
            #             or trat_dados[0] == 'FOSC' and trat_dados[1] == 'FOSC' and posicao_suvinil ==6 or \
            #             trat_dados[0] == 'PROT' and trat_dados[1] == 'ANTIBAC' and posicao_suvinil == 6 or \
            #             trat_dados[0] == 'BRI' and trat_dados[1] == 'SEDA' and posicao_suvinil ==6:
            #         codigo = trat_dados[2]
            #         acabamento = trat_dados[0]
            #         embalagem = trat_dados[7]
            #         quantidade = trat_dados[8]
            #         time.sleep(2)
            #         lista_def = [codigo, acabamento, embalagem, quantidade]
            #
            #         return lista_def
            #
            #     # ACABAMENTO COM 2 PALAVRAS E COR COM 3 PALAVRAS
            #     if trat_dados[0] == 'LIMP' and trat_dados[1] == 'FACIL' and posicao_suvinil == 7 \
            #             or trat_dados[0] == 'FOSC' and trat_dados[1] == 'DURA' == 7 or \
            #             trat_dados[0] == 'PROT' and trat_dados[1] == 'ANTIBAC' == 7 or \
            #             trat_dados[0] == 'BRI' and trat_dados[1] == 'SEDA' == 7:
            #         pt.alert('Abamento com 2 palavras E cor com 3 palavra')
            #         codigo = trat_dados[2]
            #         acabamento = trat_dados[0]
            #         embalagem = trat_dados[8]
            #         quantidade = trat_dados[9]
            #         time.sleep(2)
            #         lista_def = [codigo, acabamento, embalagem, quantidade]
            #         return lista_def
            #
        #     #
        #     #     if posicao_coral:
        #     #
        #     #         # ACABAMENTO COM 3 PALAVRAS E COR COM 3 PALAVRAS
        #     #         if trat_dados[0] == 'DEL' and trat_dados[1] == 'REN' and trat_dados[2] == 'MT' and posicao_coral == 8:
        #     #             codigo = trat_dados[3]
        #     #             acabamento = trat_dados[0]
        #     #             embalagem = trat_dados[9]
        #     #             quantidade = trat_dados[10]
        #     #             pt.alert('Abamento com 3 palavras E cor com 3 palavra')
        #     #             lista_def = [codigo, acabamento, embalagem, quantidade]
        #     #
        #     #             return lista_def
        #     #
        #     #         # ACABAMENTO COM 3 PALAVRAS E COR COM 2 PALAVRAS
        #     #         if trat_dados[0] == 'DEL' and trat_dados[1] == 'REN' and trat_dados[2] == 'MT' and posicao_coral == 7:
        #     #             codigo = trat_dados[3]
        #     #             acabamento = trat_dados[0]
        #     #             embalagem = trat_dados[7]
        #     #             quantidade = trat_dados[8]
        #     #             pt.alert('Abamento com 3 palavras E cor com 2 palavra')
        #     #             lista_def = [codigo, acabamento, embalagem, quantidade]
        #     #
        #     #             return lista_def
        #     #
        #     #         # ACABAMENTO COM 3 PALAVRAS E COR COM 1 PALAVRA
        #     #         if trat_dados[0] == 'DEL' and trat_dados[1] == 'REN' and trat_dados[2] == 'MT' and posicao_coral == 6:
        #     #             codigo = trat_dados[3]
        #     #             acabamento = trat_dados[0]
        #     #             embalagem = trat_dados[7]
        #     #             quantidade = trat_dados[8]
        #     #             pt.alert('Abamento com 3 palavras E cor com 1 palavra')
        #     #             lista_def = [codigo, acabamento, embalagem, quantidade]
        #     #
        #     #             return lista_def
        #     #         # ________________________________________________________________________________________
        #     #         # ACABAMENTO COM 2 PALAVRAS E COR COM 1 PALAVRAS
        #     #         if trat_dados[0] == 'LIMP' and trat_dados[1] == 'FACIL' and posicao_coral == 5 \
        #     #                 or trat_dados[0] == 'FOSC' and trat_dados[1] == 'DURA' and posicao_coral == 5 or \
        #     #                 trat_dados[0] == 'PROT' and trat_dados[1] == 'ANTIBAC' and posicao_coral == 5 or \
        #     #                 trat_dados[0] == 'BRI' and trat_dados[1] == 'SEDA' and posicao_coral == 5:
        #     #             time.sleep(3)
        #     #             codigo = trat_dados[2]
        #     #             acabamento = trat_dados[0]
        #     #             embalagem = trat_dados[6]
        #     #             quantidade = trat_dados[7]
        #     #
        #     #             lista_def = [codigo, acabamento, embalagem, quantidade]
        #     #             time.sleep(2)
        #     #             return lista_def
        #     #         #
        #     #         # ACABAMENTO COM 2 PALAVRAS E COR COM 2 PALAVRAS
        #     #         if trat_dados[0] == 'LIMP' and trat_dados[1] == 'FACIL' and posicao_coral == 6 \
        #     #                 or trat_dados[0] == 'FOSC' and trat_dados[1] == 'FOSC' == 6 or \
        #     #                 trat_dados[0] == 'PROT' and trat_dados[1] == 'ANTIBAC' == 6 or \
        #     #                 trat_dados[0] == 'BRI' and trat_dados[1] == 'SEDA' == 6:
        #     #             codigo = trat_dados[2]
        #     #             acabamento = trat_dados[0]
        #     #             embalagem = trat_dados[7]
        #     #             quantidade = trat_dados[8]
        #     #             time.sleep(2)
        #     #             lista_def = [codigo, acabamento, embalagem, quantidade]
        #     #
        #     #             return lista_def
        #     #
        #     #         # ACABAMENTO COM 2 PALAVRAS E COR COM 3 PALAVRAS
        #     #         if trat_dados[0] == 'LIMP' and trat_dados[1] == 'FACIL' and posicao_coral == 7 \
        #     #                 or trat_dados[0] == 'FOSC' and trat_dados[1] == 'FOSC' == 7 or \
        #     #                 trat_dados[0] == 'PROT' and trat_dados[1] == 'ANTIBAC' == 7 or \
        #     #                 trat_dados[0] == 'BRI' and trat_dados[1] == 'SEDA' == 7:
        #     #             pt.alert('Abamento com 2 palavras E cor com 3 palavra')
        #     #             codigo = trat_dados[2]
        #     #             acabamento = trat_dados[0]
        #     #             embalagem = trat_dados[8]
        #     #             quantidade = trat_dados[9]
        #     #             time.sleep(2)
        #     #             lista_def = [codigo, acabamento, embalagem, quantidade]
        #     #             return lista_def

    #['DOCUMENTO', 'DATA', 'DE', 'EMISSÃO', 'PRODUTO', 'CÓDIGO', 'REFERÊNCIA', 'MÁQUINA', 'STATUS', 'DO', 'PREPARO', 'DESCRIÇÃO', 'QUANTIDADE', 'TIPO', 'DO', 'PRODUTO', 'ORDEM', 'EMITIDA', 'ETIQUETA', 'EMITIDA', 'RESPONSÁVEL', 'TIPO', 'DO', 'PREPARO', '006/0019315-N', 'ONTEM', '2179267', 'IQ', 'ABERTO', 'LIMPA', 'FACIL', '395', 'P', 'VENTO', 'GELIDO', 'SUVINIL', '16L', '4,00', 'IMOBILIÁRIA', 'TINGIMENTO', '006/0019247-N', '08/11/2022', '2179180', 'IQ', 'ABERTO', 'LIMP', 'FACIL', '003', 'P', 'BRANCO', 'GELO', 'IQUINE', '16L', '6,00', 'IMOBILIÁRIA', 'TINGIMENTO']
        #
        # else:
        #     return 'lista_vazia'

#['DOCUMENTO', 'DATA', 'DE', 'EMISSÃO', 'TIPO', 'DE', 'ENTREGA', 'DATA', 'DE', 'ENTREGA', 'CLIENTE', 'POSIÇÃO', 'SEPARAÇÃO', 'EMPRESA', 'COLETA', 'ZONA', 'SEPARAÇÃO', 'IMPRESSA', 'STATUS', 'CONFERIDO', 'CONFERÊNCIA', 'STATUS', 'DO', 'PREPARO', '006/6054675', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'ABERTO', 'ABERTA', '006', 'FL06A2', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '006/6054674', 'HOJE', 'HOJE', 'ATACADAO', 'S/A', 'CONFERIR', 'FINALIZADA', '006', 'FL06', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '006/6054674', 'HOJE', 'HOJE', 'ATACADAO', 'S/A', 'ABERTO', 'ABERTA', '006', 'FL06A3', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054667', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'ABERTO', 'ABERTA', '001', 'DEP01', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054658-P', 'HOJE', '18/11/2022', 'I', 'SHENG', 'BRASIL', 'IND', 'E', 'COM', 'DE', 'COMP', 'ELETRONICOS', 'LTDA', 'ABERTO', 'ABERTA', '001', 'DEP04', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054655-P', 'HOJE', '18/11/2022', 'SUPER', 'G', 'TRANSP', 'E', 'LOCACAO', 'EQUIP', 'INDUSTRIAIS', 'LTDA', 'ABERTO', 'ABERTA', '001', 'DEP06', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '006/6054653', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'ABERTO', 'ABERTA', '006', 'FL06A2', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054652', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'ABERTO', 'ABERTA', '001', 'DEP06', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054652', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'CONFERIR', 'FINALIZADA', '001', 'DEP01', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6054649', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'FATURAR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6054645', 'HOJE', 'HOJE', 'NOVATEK', 'TECNOLOGIA', 'AMBIENTAL', 'LTDA', 'ABERTO', 'ABERTA', '001', 'DEP04', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054645', 'HOJE', 'HOJE', 'NOVATEK', 'TECNOLOGIA', 'AMBIENTAL', 'LTDA', 'CONFERIR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6054280-P', 'HOJE', 'HOJE', 'IBRAP', 'IND.', 'BRASILEIRA', 'DE', 'ALUMINIO', 'E', 'PLASTICOS', 'S.A', 'CONFERIR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6054280-P', 'HOJE', 'HOJE', 'IBRAP', 'IND.', 'BRASILEIRA', 'DE', 'ALUMINIO', 'E', 'PLASTICOS', 'S.A', 'ABERTO', 'ABERTA', '001', 'DEP05', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054398-P', 'HOJE', '18/11/2022', 'AMCOR', 'EMBALAGENS', 'DA', 'AMAZONIA', 'LTDA', 'ABERTO', 'ABERTA', '001', 'DEP01', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054643', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'CONFERIR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6054642', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'ABERTO', 'ABERTA', '001', 'DEP01', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '005/6048722-P', 'HOJE', '18/11/2022', 'VECTRA', 'ENGENHARIA', 'LTDA', 'CONFERIR', 'FINALIZADA', '001', 'DEP04', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6054637', 'HOJE', 'HOJE', 'R', 'M', 'L', 'DA', 'SILVA', 'EIRELI', 'FATURAR', 'FINALIZADA', '001', 'DEP04', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6048166-P', 'HOJE', '18/11/2022', 'F.A.L.', 'COMERCIO', 'DE', 'IMPORTACAO', 'E', 'EXPORTACAO', 'LTDA', 'CONFERIR', 'FINALIZADA', '001', 'DEP02', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6053850-P', 'HOJE', 'HOJE', 'COMSERVICO', 'LTDA', 'ABERTO', 'ABERTA', '001', 'DEP04', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054634', 'HOJE', 'HOJE', 'VENEZA', 'AUTO', 'POSTO', 'ABERTO', 'ABERTA', '001', 'DEP03', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054630-P', 'HOJE', 'HOJE', 'NAVEGACAO', 'RIO', 'NEGRO', 'S/A', 'FATURAR', 'FINALIZADA', '001', 'DEP05', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/5967176-P', 'HOJE', '18/11/2022', 'LEGIAO', 'DA', 'BOA', 'VONTADE', 'CONFERIR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6053202-P', 'HOJE', '18/11/2022', 'ANTONIO', 'CLEBER', 'MATIAS', 'BARROSO', 'CONFERIR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', 'FINALIZADO', '001/6030271-P', 'HOJE', '18/11/2022', 'M', 'G', 'SILVA', 'MONTEIRO', 'E', 'CIA', 'LTDA', '-', 'EPP', 'CONFERIR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6054491-P', 'HOJE', 'HOJE', 'ELETEC', 'SERVICO', 'DE', 'MANUTENCAO', 'ELETRICA', 'LTDA', 'CONFERIR', 'FINALIZADA', '006', 'FL06', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '005/0172451-S', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'EXECUTAR', 'FINALIZADA', '005', 'DOCA05', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'FINALIZADA', 'INICIADO', '001/6047927-P', 'HOJE', '18/11/2022', 'SOC.', 'MICHELIN', 'DE', 'PARTIC.', 'IND.', 'COMERCIO', 'LTDA', 'CONFERIR', 'FINALIZADA', '001', 'DEP05', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6054545-P', 'HOJE', 'HOJE', 'IJP', 'COMERCIO', 'DE', 'MOVEIS', 'LTDA', 'ABERTO', 'ABERTA', '001', 'DEP01', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054545-P', 'HOJE', 'HOJE', 'IJP', 'COMERCIO', 'DE', 'MOVEIS', 'LTDA', 'CONFERIR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6054553-P', 'HOJE', '18/11/2022', 'REFINARIA', 'DE', 'MANAUS', 'S.A', 'CONFERIR', 'FINALIZADA', '001', 'DEP04', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '006/6054536', 'HOJE', 'HOJE', 'WALDEMIRO', 'P', 'LUSTOZA', '&', 'CIA', 'LTDA', 'FATURAR', 'INICIADA', '006', 'FL06A3', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'FINALIZADA', '001/6054533-P', 'HOJE', '18/11/2022', 'MOTO', 'HONDA', 'DA', 'AMAZONIA', 'LTDA', 'ABERTO', 'ABERTA', '001', 'DEP05', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054511', 'HOJE', 'HOJE', 'E', 'A', 'H', 'EMPRESA', 'AMAZONENSE', 'DE', 'HOTELARIA', 'LTDA', 'FATURAR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'FINALIZADA', '006/6054485', 'HOJE', 'HOJE', 'JESSICA', 'SABBA', 'TAYAH', 'FATURAR', 'ABERTA', '006', 'FL06A2', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'FINALIZADA', '001/6054481-P', 'HOJE', '18/11/2022', 'SOC.', 'MICHELIN', 'DE', 'PARTIC.', 'IND.', 'COMERCIO', 'LTDA', 'ABERTO', 'ABERTA', '001', 'DEP03', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054481-P', 'HOJE', '18/11/2022', 'SOC.', 'MICHELIN', 'DE', 'PARTIC.', 'IND.', 'COMERCIO', 'LTDA', 'CONFERIR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6043425-P', 'HOJE', 'AMANHÃ', 'UNICOBA', 'ENERGIA', 'S.A', 'ABERTO', 'ABERTA', '001', 'DEP03', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054446', 'HOJE', 'HOJE', 'E', 'A', 'H', 'EMPRESA', 'AMAZONENSE', 'DE', 'HOTELARIA', 'LTDA', 'FATURAR', 'FINALIZADA', '001', 'DEP04', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'FINALIZADA', '001/6054419', 'HOJE', 'HOJE', 'L', 'J', 'GUERRA', 'E', 'CIA', 'LTDA', '-', 'FILIAL', '06', 'CONFERIR', 'FINALIZADA', '001', 'DEP07', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6053571-P', 'HOJE', '18/11/2022', 'SYRIA', 'ENGENHARIA', 'E', 'CONSTRUCAO', 'EIRELI', 'ABERTO', 'ABERTA', '001', 'DEP03', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054417', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'FATURAR', 'FINALIZADA', '001', 'DEP01', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '006/6054409-P', 'HOJE', 'HOJE', 'CONDOMINIO', 'DO', 'EDIFICIO', 'SCORPIUS', 'APART', 'HOTEL', 'SEPARAR', 'DIVERGENTE', '001', 'DEP02', 'SIM', 'ABERTO', 'DIVERGÊNCIA', 'SEPARAÇÃO', 'ABERTA', '006/6054409-P', 'HOJE', 'HOJE', 'CONDOMINIO', 'DO', 'EDIFICIO', 'SCORPIUS', 'APART', 'HOTEL', 'CONFERIR', 'DIVERGENTE', '001', 'DEP02', 'SIM', 'ABERTO', 'DIVERGÊNCIA', 'SEPARAÇÃO', 'ABERTA', '001/6054400', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'FATURAR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '006/6054377-P', 'HOJE', '18/11/2022', 'COMPASSO', 'CONSTR', ',TERRAPLANAGEM', 'E', 'PAVIMENTACAO', 'LTDA', 'CONFERIR', 'FINALIZADA', '001', 'DEP03', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6054065-P', 'HOJE', 'HOJE', 'NAVEMAZONIA', 'NAVEGACAO', 'LTDA', 'CONFERIR', 'FINALIZADA', '001', 'DEP03', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '006/6054337', 'HOJE', 'HOJE', 'L', 'J', 'GUERRA', 'E', 'CIA', 'LTDA', 'ABERTO', 'ABERTA', '006', 'FL06A1', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '006/6054337', 'HOJE', 'HOJE', 'L', 'J', 'GUERRA', 'E', 'CIA', 'LTDA', 'CONFERIR', 'FINALIZADA', '006', 'FL06A2', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6054270', 'HOJE', 'HOJE', 'MAQMOTO-MAQUINAS', 'E', 'MOTORES', 'LTDA', 'FATURAR', 'FINALIZADA', '001', 'DEP03', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6054268', 'HOJE', 'HOJE', 'SUELLEN', 'GUIMARAES', 'SOARES', 'FATURAR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6054253-P', 'HOJE', '18/11/2022', 'MITSUBA', 'DO', 'BRASIL', 'LTDA', 'CONFERIR', 'FINALIZADA', '001', 'DEP03', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6053971-P', 'HOJE', '18/11/2022', 'CONDOMINIO', 'RESIDENCIAL', 'ESPANHA', 'CONFERIR', 'FINALIZADA', '001', 'DEP05', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6054237', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'FATURAR', 'FINALIZADA', '001', 'DEP03', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6054222-P', 'HOJE', '18/11/2022', 'AMAZON', 'MILK', 'INDUSTRIA', 'E', 'COMERCIO', 'LTDA', 'ABERTO', 'ABERTA', '001', 'DEP03', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6054150-P', 'HOJE', 'HOJE', 'PERES', 'E', 'SANTOS', 'LTDA', 'FATURAR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'COM', 'DIVERGÊNCIA', 'DIVERGENTE', '001/6054150-P', 'HOJE', '18/11/2022', 'PERES', 'E', 'SANTOS', 'LTDA', 'FATURAR', 'FINALIZADA', '001', 'DEP05', 'SIM', 'ABERTO', 'COM', 'DIVERGÊNCIA', 'DIVERGENTE', '001/6054025-P', 'HOJE', '18/11/2022', 'DELTA', 'MAQUINAS', 'LTDA', 'CONFERIR', 'FINALIZADA', '001', 'DEP05', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6054026', 'HOJE', 'HOJE', 'MAHY', 'CERVEJARIA', 'IND.', 'E', 'COM.', 'DE', 'BEBIDAS', 'LTDA', 'FATURAR', 'FINALIZADA', '001', 'DEP05', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '005/6053942', 'HOJE', 'HOJE', "MARK'S", 'ENGENHARIA', 'EIRELI', 'CONFERIR', 'FINALIZADA', '005', 'MEZANINO05', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6053910-P', 'HOJE', 'HOJE', 'ALEGRA', 'INDUSTRIA', 'E', 'COMERCIO', 'LTDA', 'FATURAR', 'FINALIZADA', '001', 'DEP06', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6053721-P', 'HOJE', '18/11/2022', 'HM', 'CONSULTORIA', 'E', 'RECURSOS', 'HUMANOS', '-', 'EIRELI', 'CONFERIR', 'FINALIZADA', '001', 'DEP05', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6046439-P', 'HOJE', '18/11/2022', 'ORIGEM', 'INDUSTRIA', 'E', 'COMERCIO', 'DE', 'MOTOS', 'LTDA.', 'CONFERIR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '006/6053775', 'HOJE', 'HOJE', 'L', 'J', 'GUERRA', 'E', 'CIA', 'LTDA', 'CONFERIR', 'FINALIZADA', '006', 'FL06A2', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '006/6053775', 'HOJE', 'HOJE', 'L', 'J', 'GUERRA', 'E', 'CIA', 'LTDA', 'ABERTO', 'ABERTA', '006', 'FL06A3', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6053737-P', 'HOJE', '18/11/2022', 'SIX', 'LABEL', 'INDUSTRIA', 'GRAFICA', 'DA', 'AMAZONIA', 'LTDA', 'CONFERIR', 'FINALIZADA', '001', 'DEP04', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6053737-P', 'HOJE', '18/11/2022', 'SIX', 'LABEL', 'INDUSTRIA', 'GRAFICA', 'DA', 'AMAZONIA', 'LTDA', 'SEPARAR', 'DIVERGENTE', '001', 'LOJA', 'SIM', 'ABERTO', 'DIVERGÊNCIA', 'SEPARAÇÃO', 'ABERTA', '005/6053399-P', 'HOJE', 'HOJE', 'PRISMA', 'SOLUCOES', 'INDUSTRIAIS', 'EIRELI', 'FATURAR', 'FINALIZADA', '001', 'DEP03', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6053603', 'HOJE', 'HOJE', 'CONSUMIDOR', 'FINAL', 'FATURAR', 'FINALIZADA', '001', 'DEP05', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6053511-P', 'HOJE', 'HOJE', 'R', 'J', 'FRANCO', 'DA', 'SILVA', 'LTDA', 'FATURAR', 'FINALIZADA', '001', 'DEP01', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6053527-P', 'HOJE', '18/11/2022', 'PRODAM-PROCESSAMENTO', 'DE', 'DADOS', 'AMAZONAS', 'SA', 'CONFERIR', 'FINALIZADA', '001', 'DEP03', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6053482', 'HOJE', 'HOJE', 'PHILCO', 'ELETRONICOS', 'S/A', 'FATURAR', 'FINALIZADA', '001', 'DEP03', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6053453', 'HOJE', 'HOJE', 'VIACAO', 'CARAVELAS', 'LTDA', 'FATURAR', 'FINALIZADA', '001', 'DEP04', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6053284-P', 'HOJE', 'HOJE', 'MARTINS', 'COMERCIO', 'E', 'SERVICOS', 'DE', 'DISTRIBUICAO', 'S/A', 'ABERTO', 'ABERTA', '001', 'DEP03', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/6053017', 'ONTEM', 'ONTEM', 'ANTONIO', 'CLEBER', 'MATIAS', 'BARROSO', 'FATURAR', 'FINALIZADA', '001', 'DEP02', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'FINALIZADA', '001/6051444-P', '14/11/2022', '14/11/2022', 'SUPERMERCADOS', 'DB', 'LTDA', '-', 'LJ', '01', 'FATURAR', 'FINALIZADA', '001', 'DEP03', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6051594-P', '14/11/2022', '14/11/2022', 'VILA', 'OLIMPIA', 'EMPREENDIMENTOS', 'IMOBILIARIOS', 'LTDA', 'FATURAR', 'FINALIZADA', '001', 'DEP03', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6049956-P', '14/11/2022', '14/11/2022', 'COMERCIO', 'E', 'NAVEGACAO', 'PRATES', 'LTDA', 'FATURAR', 'FINALIZADA', '001', 'DEP01', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '005/6050643-P', '14/11/2022', '14/11/2022', 'ANA', 'CAROLINE', 'PENZ', 'FATURAR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6049575', '12/11/2022', '12/11/2022', 'CONSUMIDOR', 'FINAL', 'FATURAR', 'FINALIZADA', '001', 'DEP01', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6049408-P', '11/11/2022', '13/11/2022', 'ASSOC.CONDOMINIO', 'DO', 'SUMAUMA', 'PARK', 'SHOPPING', '-ACSPS', 'CONFERIR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6049408-P', '11/11/2022', '13/11/2022', 'ASSOC.CONDOMINIO', 'DO', 'SUMAUMA', 'PARK', 'SHOPPING', '-ACSPS', 'SEPARAR', 'DIVERGENTE', '001', 'DEP04', 'SIM', 'ABERTO', 'DIVERGÊNCIA', 'SEPARAÇÃO', 'ABERTA', '001/6048198-P', '11/11/2022', '13/11/2022', 'BRIDGE', 'IND.DE', 'PRODUTOS', 'PLASTICOS', 'DA', 'AMAZONIA', 'LTDA', 'ABERTO', 'FINALIZADA', '001', 'DEP01', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '006/6047376', '10/11/2022', '10/11/2022', 'BEMOL', 'S/A', 'FATURAR', 'ABERTA', '006', 'FL06A1', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'FINALIZADA', '005/6046537', '10/11/2022', '10/11/2022', 'CICLO', 'CAIRU', 'DISTRIB.', 'PECAS', 'PARA', 'MOTOCICLETAS', 'LTDA', 'ABERTO', 'FINALIZADA', '005', 'FL05', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6046404-P', '10/11/2022', '12/11/2022', 'AGROPECUARIA', 'JAYORO', 'LTDA', 'FATURAR', 'FINALIZADA', '001', 'DEP01', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6044416-P', '10/11/2022', '11/11/2022', 'EULIS', 'DOS', 'SANTOS', 'COSTA', 'FATURAR', 'FINALIZADA', '001', 'DEP07', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6039151-P', '09/11/2022', '10/11/2022', 'PROCOMP', 'AMAZONIA', 'INDUSTRIA', 'ELETRONICA', 'LTDA', 'CONFERIR', 'FINALIZADA', '001', 'LOJA', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6042426-P', '08/11/2022', '08/11/2022', 'COMSERVICO', 'LTDA', 'CONFERIR', 'FINALIZADA', '006', 'FL06A2', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6031131', '29/10/2022', '29/10/2022', 'CONSUMIDOR', 'FINAL', 'FATURAR', 'FINALIZADA', '001', 'DEP01', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6030906', '29/10/2022', '29/10/2022', 'CONSUMIDOR', 'FINAL', 'FATURAR', 'FINALIZADA', '001', 'DEP07', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '005/6030829', '29/10/2022', '29/10/2022', 'L', 'J', 'GUERRA', 'E', 'CIA', 'LTDA', '-', 'FILIAL', '05', 'CONFERIR', 'FINALIZADA', '005', 'FL05', 'SIM', 'ABERTO', 'EM', 'CONFERÊNCIA', 'ABERTA', '001/6026800-P', '26/10/2022', '26/10/2022', 'THERMO', 'NORTE', 'COM.', 'PECAS', 'E', 'SERV.', 'REFRIGERACAO', 'LTDA', 'FATURAR', 'FINALIZADA', '006', 'FL06A3', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/6026179', '26/10/2022', '26/10/2022', 'CONSUMIDOR', 'FINAL', 'FATURAR', 'FINALIZADA', '001', 'DEP01', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '005/6024141', '25/10/2022', '25/10/2022', 'L', 'J', 'GUERRA', 'E', 'CIA', 'LTDA', 'ABERTO', 'ABERTA', '005', 'FL05', 'SIM', 'ABERTO', 'EM', 'SEPARAÇÃO', 'ABERTA', '001/5986720', '27/09/2022', '28/09/2022', 'CONSUMIDOR', 'FINAL', 'CONFERIR', 'FINALIZADA', '001', 'DEP01', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '005/5973835-P', '17/09/2022', '17/09/2022', 'CONSUMIDOR', 'FINAL', 'FATURAR', 'FINALIZADA', '006', 'FL06', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', '001/0258464-W', '21/02/2022', '21/02/2022', 'MAYCON', 'ARAUJO', 'DA', 'SILVA', 'FATURAR', 'FINALIZADA', '001', 'DEP02', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', 'ABERTO', '006/0087965-C', '21/02/2022', '21/02/2022', 'CONSUMIDOR', 'FINAL', 'FATURAR', 'FINALIZADA', '006', 'FL06A3', 'SIM', 'ABERTO', 'CONFERIDO', 'FINALIZADA', 'ABERTO']



#['DOCUMENTO', 'DATA', 'DE', 'EMISSÃO', 'TIPO', 'DE', 'ENTREGA', 'PRODUTO', 'MÁQUINA', 'STATUS', 'DO', 'PREPARO', 'DESCRIÇÃO', 'QUANTIDADE', 'ORDEM', 'EMITIDA', 'ETIQUETA', 'EMITIDA', 'TIPO', 'DO', 'PRODUTO', 'TIPO', 'DO', 'PREPARO', 'RESPONSÁVEL', '001/0244725-W', '12/01/2022', '2164122', '_P', 'ABERTO', 'ACAB', 'SEDA', 'BRANCO', 'CONTEMPORA', '20YY', '66', '066', '5167', 'P16L']
