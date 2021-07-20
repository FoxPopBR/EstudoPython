#-*- coding: -utf8 -*-
import os
NomePlayer = ["andreribei00","andreribeir0","AquelaSereia","BangTan 7","Ben Reilly","BlackWidowMF","BR WOLVERINE","Catotinha","dhyessika","Duffly","Fabiiano","FoxPop","Green Vile","hvReus","JEFFER132","Junior crvg","KRATOS 79 BR","KRATOS BR MF","Lady Catota","lalinha44","Lightside 1","Lord Costela","LordRafaeel","MadMax420","MadMoustache","MeniPlays","isaveio","Mx Julielton","Nioljso","O Pae Ta On","princepesam","Rainha Agnes","Rasanzi,Sammy A","Smith Master","sunsupershin","UM DOIS 1 2","Vanda mob","willrick001","Wolverine BR","xX pipoca Xx","xX SAC Xx","xXsaquinXx"] #Lista de membros da guild, separados.. cada nome um item da lista
dig = 0
digop = ""
op = (int)
qt = len(NomePlayer)


def menuo ():
    os.system('cls') #chama comando do sistema operacional, no caso o comando "cls"
    dig = 0
    digop = ""
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
    dig = input("escolha uma opção: ")


if dig == 1:
    digop = input("Digite o nome do membro: ")  
    if digop in NomePlayer == True:
        print("O jogador:",digop,"é um membro da guild!")
        input()
        menuo()
    elif digop in NomePlayer == False:
        print("O jogador:",digop,"não faz parte da guild!")
        input()
        menuo()
elif dig == 2:
    print("Quantidade de membros da guild:",qt)
    input()   
    menuo()
elif dig == 3:
    os.system('cls')
    print("Fechando tudo.. Bye")
    input()
else:
    print("Você entendeu as opções? Faça direito!")
    input()
    menuo()


menuo()
 



