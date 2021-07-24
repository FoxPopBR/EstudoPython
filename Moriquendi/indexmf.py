#-*- coding: -utf8 -*-
""" [summary]
Todas as descrições em breve!

Todas as funções criadas em classMF
@ Teste --------> Somente para testes rápidos
@ ListaPlayer --> Gera lista de Jogadores cadastrados com id
@ MenuLM -------> Desenho do MENU sem interatividade cadastro, remover, buscar, lista, Jogadores
@ Escolha ------> Local para interagir com opções do menu, manipulação de variáveis e parte lógica da interface 
@ MenuCad ------> Escolhas do MenuLM / MENU cadastro, remover, buscar, lista, Jogadores
@ Menuo --------> Parte grafica do menu sem interatividade, chama automáticamente a função Escolha

    [extended_summary]
By FoxPop / FabioCesar
"""
import os
import sys
from classMF.packMF import *

while True:
    os.system("cls")
    Menuo() #Inicia o programa 
 
 