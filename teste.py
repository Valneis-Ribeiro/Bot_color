# from pyautogui import alert
#
# trat_dados = ['DOCUMENTO', 'DATA', 'DE', 'EMISSÃO', 'PRODUTO', 'CÓDIGO', 'REFERÊNCIA', 'MÁQUINA', 'STATUS', 'DO', 'PREPARO', 'DESCRIÇÃO', 'QUANTIDADE', 'TIPO', 'DO', 'ORDEM', 'EMITIDA', 'ETIQUETA', 'EMITIDA', 'RESPONSÁVEL', 'TIPO', 'DO', 'PREPARO', '006/0106389-C', 'HOJE', '2179230', 'IQ', 'ABERTO', 'LIMP', 'FACIL' ,'1249', 'P', 'URUAÇU','IQUINE', '3,200L', '2,00', 'IMOBILIÁRIA', 'TINGIMENTO', '006/0019247-N', 'ONTEM', '2179180', 'IQ', 'ABERTO', 'LIMP', 'FACIL', '003', 'P', 'BRANCO', 'GELO', 'IQUINE', '16L', '6,00', 'IMOBILIÁRIA', 'TINGIMENTO', '006/0106145-C', '05/11/2022', '2179114', 'IQ', 'ABERTO', 'LIMP','FACIL' '1249', 'P', 'URUACU', 'IQUINE', '3,200L', '1,00', 'IMOBILIÁRIA', 'TINGIMENTO']
#
# # pegar a primeira de pedido
# trat_dados = trat_dados[:39]
# trat_dados = trat_dados[29:]
#
# #['006/0106389-C', 'HOJE', '2179230', 'IQ', 'ABERTO', 'LIMP', 'FACIL', '1249', 'P', 'URUACU', 'IQUINE', '3,200L', '2,00', 'IMOBILIÁRIA', 'TINGIMENTO']
#
# print(trat_dados)
#
# posicao_iquine = trat_dados.index('IQUINE')
#
# print(posicao_iquine)
#
#
#
# # ACABAMENTO COM 3 PALAVRAS E COR COM 3 PALAVRAS
# if trat_dados[0] == 'DEL' and trat_dados[1] == 'REN' and trat_dados[2] =='MT' and posicao_iquine == 8:
#         codigo = trat_dados[3]
#         acabamento = trat_dados[0]
#         embalagem = trat_dados[9]
#         quantidade = trat_dados[10]
#         alert('Abamento com 3 palavras E cor com 3 palavra')
#         lista_def = [codigo, acabamento, embalagem, quantidade]
#         print(lista_def)
#
#
# # ACABAMENTO COM 3 PALAVRAS E COR COM 2 PALAVRAS
# if trat_dados[0] == 'DEL' and trat_dados[1] == 'REN' and trat_dados[2] =='MT' and posicao_iquine == 7:
#         codigo = trat_dados[3]
#         acabamento = trat_dados[0]
#         embalagem = trat_dados[7]
#         quantidade = trat_dados[8]
#         alert('Abamento com 3 palavras E cor com 2 palavra')
#         lista_def = [codigo, acabamento, embalagem, quantidade]
#         print(lista_def)
#
#
#
# # ACABAMENTO COM 3 PALAVRAS E COR COM 1 PALAVRA
# if trat_dados[0] == 'DEL' and trat_dados[1] == 'REN' and trat_dados[2] =='MT' and posicao_iquine == 6:
#         codigo = trat_dados[3]
#         acabamento = trat_dados[0]
#         embalagem = trat_dados[7]
#         quantidade = trat_dados[8]
#         alert('Abamento com 3 palavras E cor com 1 palavra')
#         lista_def = [codigo, acabamento, embalagem, quantidade]
#         print(lista_def)
#
# #________________________________________________________________________________________
#
# # ACABAMENTO COM 2 PALAVRAS E COR COM 1 PALAVRAS
# if trat_dados[0] == 'LIMP' and trat_dados[1] == 'FACIL'  and posicao_iquine == 5 \
#         or trat_dados[0] == 'FOSC' and trat_dados[1] == 'FOSC' == 5 or \
#         trat_dados[0] == 'PROT' and trat_dados[1] == 'ANTIBAC' == 5 or \
#         trat_dados[0] == 'BRI' and trat_dados[1] == 'SEDA' == 5:
#         alert('Abamento com 2 palavras E cor com 1 palavra')
#         codigo = trat_dados[2]
#         acabamento = trat_dados[0]
#         embalagem = trat_dados[6]
#         quantidade = trat_dados[7]
#         lista_def = [codigo, acabamento, embalagem, quantidade]
#         print(lista_def)
#
#
# # ACABAMENTO COM 2 PALAVRAS E COR COM 2 PALAVRAS
# if trat_dados[0] == 'LIMP' and trat_dados[1] == 'FACIL'  and posicao_iquine == 6 \
#         or trat_dados[0] == 'FOSC' and trat_dados[1] == 'FOSC' == 6 or \
#         trat_dados[0] == 'PROT' and trat_dados[1] == 'ANTIBAC' == 6 or \
#         trat_dados[0] == 'BRI' and trat_dados[1] == 'SEDA' == 6:
#         alert('Abamento com 2 palavras E cor com 2 palavra')
#         codigo = trat_dados[2]
#         acabamento = trat_dados[0]
#         embalagem = trat_dados[7]
#         quantidade = trat_dados[8]
#         lista_def = [codigo, acabamento, embalagem, quantidade]
#         print(lista_def)
#
#
#
# # ACABAMENTO COM 2 PALAVRAS E COR COM 3 PALAVRAS
# if trat_dados[0] == 'LIMP' and trat_dados[1] == 'FACIL'  and posicao_iquine == 7 \
#         or trat_dados[0] == 'FOSC' and trat_dados[1] == 'FOSC' == 7 or \
#         trat_dados[0] == 'PROT' and trat_dados[1] == 'ANTIBAC' == 7 or \
#         trat_dados[0] == 'BRI' and trat_dados[1] == 'SEDA' == 7:
#         alert('Abamento com 2 palavras E cor com 3 palavra')
#         codigo = trat_dados[2]
#         acabamento = trat_dados[0]
#         embalagem = trat_dados[8]
#         quantidade = trat_dados[9]
#         lista_def = [codigo, acabamento, embalagem, quantidade]
#         print(lista_def)
#
#
#
#
#
#
#
#






# elif trat_dados[5]=='LIMP'and trat_dados=='FACIL':


# #GABARITO cor 1 palavra e acabamento com  2 palavras
# elif posicao_iquine == 10:
#     alert('Cor com 1 PALAVRAS')
#     codigo = trat_dados[7]
#     acabamento = trat_dados[5]
#     embalagem = trat_dados[11]
#     quantidade = trat_dados[12]
#     lista_def = [codigo, acabamento, embalagem, quantidade]
#     print(lista_def)
#
# #GABARITO cor com 2 palavras e acabamento com 2 palavras
# if posicao_iquine == 11:
#     alert('Cor com 2 PALAVRAS')
#     codigo = trat_dados[7]
#     acabamento = trat_dados[5]
#     embalagem = trat_dados[12]
#     quantidade = trat_dados[13]
#     lista_def = [codigo, acabamento, embalagem, quantidade]
#     print(lista_def)
#
# #
# #GABARITO cor com 3 palavras e acabamento com 2 palavras
# elif posicao_iquine == 12:
#     alert('Cor com 3 PALAVRAS')
#     codigo = trat_dados[7]
#     acabamento = trat_dados[5]
#     embalagem = trat_dados[13]
#     quantidade = trat_dados[14]
#     lista_def = [codigo, acabamento, embalagem, quantidade]
#     print(lista_def)

import os

usuarios = os.environ

print(usuarios['USERNAME'])
