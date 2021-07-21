# -*- coding: utf-8 -*-
""" [Bibliotecas - Pacotesde - Funções]
- Aqui são criadas todas as funções e derivados
@ Menuo   --> Parte grafica do menu sem interatividade, chama automáticamente a função Escolha
@ Escolha --> Local para interagir com opções do menu, manipulação de variáveis e parte lógica da interface 

    [extended_summary]
- Novas funções e derivadas serão criadas aqui!
    """
import os
import sys
from time import sleep, time
from tracemalloc import stop
from corpomf import * #arquivo onde contem todas as variáveis global

def Escolha():
    global opcao,contador # Variável precisa ser declarada dentro da função como global para ser modificada
    opcao = input("Escolha uma opção: " ) #Escolhendo uma opção no menu
    contador = contador + 1
    if opcao == "1":    #Inicio das opções do Menu inicial
        digop = input ("Digite o nome do jogador: ")
        if digop in NomePlayer:
            print("O jogador:",digop,"é um membro da guild!")
            input("Enter P/ Continuar..")   
            Menuo()  
        else:  
            print("O jogador:",digop,"não faz parte da guild!")
            input("Enter P/ Continuar..")
            Menuo()  
    elif opcao == "2":
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
    
    
def Menuo(): #Função para desenhar o menu simples
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



