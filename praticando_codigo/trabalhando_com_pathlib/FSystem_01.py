# -*- coding: utf-8 -*-
"""
Testes com pathlib para manipuação do
File System (Diretorios, subsdiretórios, etc...)

Checando a existencia do home de trabalho COM 
o arquivo de entrada tree.txt
e do subdiretório de trabalho de saida ./TREE
já deixa pronto o path do arquivo de entrada -> ./tree.txt
e o do arquivo de saida -> .\TREE\resultado_01.txt


"""
import pathlib
in_file = pathlib.Path('tree.txt') # arquivo onde estão os dados
home_path = pathlib.Path('.') # diretorio home
work_in = home_path / in_file # concatenando home & arquivo de daos para o open
work_path = pathlib.Path('./TREE') #path dos arquivos de saída
out_file = pathlib.Path('resultado_01.txt') # nome do arquivo de saida
work_out = work_path / out_file # concatenando path de saida com o arquivo de saida
#
# Testa a existencia do arquivo de entrada e do subdiretório dedos arquivos d saida
#
tudo_ok = True
if work_in.exists() == False:
    print("Falta o arquivo com os dados de entrada --> tree.txt")
    tudo_ok = False
if work_path.exists() == False:
    print("Falta o subdiretório dos arq´s de saida --> ./TREE")
    tudo_ok = False
if tudo_ok == True:
    print("Vamos em frente")
    






