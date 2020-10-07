# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 07:19:09 2020

Testes com pathlib para manipuação do
File System (Diretorios, subsdiretórios, etc...)

===> execução dos exemplos encontrados no 
arquivo -> 
"D:\SANDBOX_GERAL\DOCUMENTAÇÃO DE ESTUDO\PYTHON\PATHLIB\
    Python - Files I_O - Tutorialspoint.pdf"

"""
# printing to screen
# print "Python is really a great language,","isn´t it?"
"""
Ao executar, reclamou que falta o parentese - abaixo funcionou.
"""
print("Python is really a great language,","isn´t it?")

# Reading Keyboard input
#str = raw_input("Enter your input: ")
#print("received input is: ",str)
"""
Ao executar, reclamou name 'raw_input' is not defined.
Esta função foi retirada da versão 3.8
Abaixo funcionou - mas veja que interessante quando se digita
como input o string '[x*5 for x in range(2,10,2)]'
se usarmos eval() ao fazer o segundo print...

a expressão quer dizer: para cada valor 'x' em range(2,10,2), começando do 2 e
indo até o 10 - pulando de 2 em dois), multiplique o 'x' por 5.
    o range() devolve sequencialmente os valores 2,4,5 e 8 para o 'x' que é
    multiplicado por 5; chegando no 10 o range() para!!!
"""
str = input("Enter your input: ")
print("Sem eval() received input is: ",str)
print("Com eval() received input is: ",eval(str))

"""
PARANDO POR AQUI - CRIANDO NOVO ARUIVO DE TESTES FSysytem)04.py
    
Daqui pra frente o diretório base (root) para brincar será 
D:\SANDBOX_GERAL\JUPYTER_SANDBOX\Raiz-do-Python\praticando_codigo\trabalhando_com_pathlib

A partir daqui vou abandonar a apostila acima pois é do tempo do python versão 2
"""



