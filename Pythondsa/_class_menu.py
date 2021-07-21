# -*- coding: utf-8 -*-
import os
from menu_corpo import NomePlayer,qt,contador
from index import opcao

def escolha():
    print("Opção escolhida:",opcao)
    if opcao == "1":
        digop = input ("Digite o nome do jogador: ")
        if digop in NomePlayer:
            print("O jogador:",digop,"é um membro da guild!")
            input() 
            menuo()  
        else:   #digop in NomePlayer == False:
            print("O jogador:",digop,"não faz parte da guild!")
            input()
            menuo()  
    elif opcao == "2":
        print("Quantidade de membros da guild:",qt)     
        input()
        menuo() 
    elif opcao == "0":
        print("digito 0 zero", opcao)
        input()
        menuo() 
    else:
        print("Você entendeu as opções? Faça direito!")
        print("digito salvo: ",opcao)
        input()
        menuo()
    
    
def menuo():
    os.system('cls') #chama comando do sistema operacional, no caso o comando "cls"
    print("Iniciando treinamento Python\nProjeto controle Moriquendi Federation")
    print("===================================================================")
    print("==                                                               ==")
    print("==                    Moriquendi Federation                      ==")
    print("==                                                               ==")
    print("==  1- Procurar Membro                                           ==")
    print("==  2- Quantidade de Membros                                     ==")
    print("==  3- Fechar                                                    ==")
    print("==                                                               ==")
    print("===================================================================\n")
    print("contador:",contador)
