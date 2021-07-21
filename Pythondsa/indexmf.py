#-*- coding: -utf8 -*-
import os
from classmf import (menuo,escolha)
from corpomf import contador,opcao
opcao = ""

while True:
    menuo()
    contador = contador + 1
    
    opcao = input("digite:")
    
    if opcao != "3":
        escolha()
    else:
       os.system('cls')
       print("Fechando tudo.. Bye") 
       break
