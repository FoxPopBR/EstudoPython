#-*- coding: -utf8 -*-
import os
from _class_menu import (menuo,escolha)
from menu_corpo import contador,opcao
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
