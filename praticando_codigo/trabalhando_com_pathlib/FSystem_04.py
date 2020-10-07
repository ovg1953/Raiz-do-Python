# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 09:12:04 2020
@author: ovgalva

CRIANDO NOVO ARUIVO DE TESTES FSysytem)04.py
    
Daqui pra frente o diretório base (root) para brincar será 
D:\SANDBOX_GERAL\JUPYTER_SANDBOX\Raiz-do-Python\praticando_codigo\trabalhando_com_pathlib

A partir daqui vou abandonar a apostila acima pois é do tempo do python versão 2
usando...

"""
# trabalhando com as bibliotecas 'os' e 'pathlib'
#from os import *
from pathlib import Path
import sys
folder = '.' # o folder é o path corrente
#filepaths1 = os.listdir(folder) # get arquivos e diretorios filho
# retorna ['FSystem_01.py', 'FSystem_02.py', 'FSystem_03.py',
# 'FSystem_04.py', 'tree.txt', 'tree_out']
#print(filepaths1,end='\n\n')
"""
 os.path.join(folder,f) concatena ao nome do path corrente
 com cada nome de arquivo/diretorio filho
 atenção --> não usar concatenação com de folder com '\'
 pois se rodar no linux teria que trocar para '/' 
"""
#filepaths2 = [os.path.join(folder, f) for f in os.listdir(folder)]
#print(filepaths2)
"""
retornou:
['.\\FSystem_01.py', '.\\FSystem_02.py', '.\\FSystem_03.py',
 '.\\FSystem_04.py', '.\\tree.txt', '.\\tree_out']    

Daqui  pra frente vou testar os metodos e instancias do modulo pathlib, 
conforme o manual da python.org
"""
