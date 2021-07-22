# -*- coding: utf-8 -*-
""" [Bibliotecas - Pacotesde - Funções]
- Aqui são criadas todas as funções e derivados
@ Menuo   --> Parte grafica do menu sem interatividade, chama automáticamente a função Escolha
@ Escolha --> Local para interagir com opções do menu, manipulação de variáveis e parte lógica da interface 

    [extended_summary]
- Novas funções e derivadas serão criadas aqui!
    """
import os
from socket import ntohl
import sys
from time import sleep, time
from tracemalloc import stop
from VarGlobal import * 
#arquivo onde contem todas as variáveis global
def ListaPlayer():
    global NomePlayer
    os.system("cls")
    for i in range(qt):
        print("ID:",IdJogador[i],"",NomePlayer[i])

# Opções de Menu Inicial
def Escolha():
    global opcao,contador # Variável precisa ser declarada dentro da função como global para ser modificada
    input("Escolha uma opção: ",opcao) #Escolhendo uma opção no menu
    contador = contador + 1
    if opcao == "1":    #Inicio das opções do Menu inicial  <------------
        MenuLM()
        opcao = ""
        input("Escolha uma opção: ",opcao) #Escolhendo uma opção no menuLM pesquisa de membros
        if opcao == "1":
            input("Buscar Nome:",digop)
            if digop in NomePlayer == True:
                print("O jogador:",digop,"é um membro da guild!")
                input("Enter P/ Continuar..")   
                MenuLM()  
            else:  
                print("O jogador:",digop,"não faz parte da guild!")
                input("Enter P/ Continuar..")
                MenuLM()
        elif opcao == "2":
            print("Implementando essa opção, tente mais tarde")
            MenuLM()
        elif opcao == "3":
            ListaPlayer()
            input("Enter P/ Continuar..")
            MenuLM()
        elif opcao == "4":
            nt = ""
            print("**************************************************************")
            print("*** Insira o nome do jogador a ser add na lista de membros ***")
            print("***                                                        ***")
            input("***Digite o nome:",nt,                                    "***")
            NomePlayer.append(nt)
            os.system("cls")
            print("**************************************************************")
            print("*** Insira o nome do jogador a ser add na lista de membros ***")
            print("***                                                        ***")
            input("*** Jogador",nt," foi adicionado com sucesso!              ***")
            input("Aperte Enter para retornar...")
            nt = ""
            MenuLM()
        if opcao == "5":
            nt = ""
            print("Digite o nome a ser removido da lista de jogadores\n")
            input("Digite o Nome:",nt)
            NomePlayer.remove(nt)
            print("O nome do Jogador ",nt," Foi removida da lista de membros!")
            nt = ""
            input("Aperte Enter para retornar...")
            MenuLM()
        if opcao == "6":
            print("retornando ao meu principal")
            sleep(1.3)
            Menuo()
        else:  # Sempre que não digitar uma opção valida
            print("Você entendeu as opções? Faça direito!")
            print("Você digitou: ",opcao)
            input("Enter P/ Continuar..")
            MenuLM()            
    elif opcao == "2":      # ------------> Continua a opção 2 do menu principal
        print("Quantidade de membros da guild:",qt)     
        input("Enter P/ Continuar..")
        Menuo()
    elif opcao == "3": # Unico jeito de parar o programa é escolhendo a opção 3 do menu
        os.system("cls")
        print("Desligando e fechando tudo.")
        sleep(2)
        os.system("cls")
        print("Bye ,o/")
        sleep(1)
        quit()        
    else:   # Sempre que não digitar uma opção valida
        print("Você entendeu as opções? Faça direito!")
        print("Você digitou: ",opcao)
        input("Enter P/ Continuar..")
        Menuo()
    
# Menu Inicial Aparência 

def Menuo(): #Função para desenhar o menu simples       -----> MENU PRINCIPAL  <------
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
    print("Opções escolhidas:",contador,"\n")
    Escolha()


def MenuLM(): #Função para desenhar o menu simples      ------> Procurar Jogadores <--------
    os.system('cls') #chama comando do sistema operacional, no caso o comando "cls"
    print("Iniciando treinamento Python\nProjeto controle Moriquendi Federation")
    print("===================================================================")
    print("==                                                               ==")
    print("==                    Moriquendi Federation                      ==")
    print("==                                                               ==")
    print("==  1- Procurar Jogador por Nome                                 ==")
    print("==  2- Procurar Jogador por ID                                   ==")
    print("==  3- Mostrar lista de jogador                                  ==")
    print("==  4- Add nome de Jogador                                       ==")
    print("==  5- Remover nome de Jogador                                   ==")
    print("==  6- Retornar ao menu principal                                ==")
    print("==                                                               ==")
    print("===================================================================\n")
    print("Opções escolhidas:",contador,"\n")
    Escolha()


