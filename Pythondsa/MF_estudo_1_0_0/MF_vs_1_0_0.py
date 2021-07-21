#-*- coding: -utf8 -*-
import os

NomePlayer = ["andreribei00","andreribeir0","AquelaSereia","BangTan 7","Ben Reilly","BlackWidowMF","BR WOLVERINE","Catotinha","dhyessika","Duffly","Fabiiano","FoxPop","Green Vile","hvReus","JEFFER132","Junior crvg","KRATOS 79 BR","KRATOS BR MF","Lady Catota","lalinha44","Lightside 1","Lord Costela","LordRafaeel","MadMax420","MadMoustache","MeniPlays","isaveio","Mx Julielton","Nioljso","O Pae Ta On","princepesam","Rainha Agnes","Rasanzi,Sammy A","Smith Master","sunsupershin","UM DOIS 1 2","Vanda mob","willrick001","Wolverine BR","xX pipoca Xx","xX SAC Xx","xXsaquinXx"] #Lista de membros da guild, separados.. cada nome um item da lista
contador = 1
digop = ""
qt = len(NomePlayer)
opcao = ""


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
    #print("Escolha uma opção: ")

while True:
    menuo()
    contador = contador + 1
    opcao = input("digite:")
    if opcao == "3":
       os.system('cls')
       print("Fechando tudo.. Bye") 
       break
    else:
        escolha()