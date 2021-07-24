#-*- coding: -utf8 -*-
""" 
    [>> Organograma Moriquendi INI <<]
My first study version of Python.

    Versionamentos Prontos


--> MF_vs_1.0.0 data 07/21/2021

lasted update >> 17:00 date 07/23/2021 <<

Initial scope of the project:

Control of members with registrations of players and guild activities, manipulation of registered data. Innovations in the project scope and implementations of new technologies and API's!
Version 1.0.0 ( 6 / 8 ) -----o--* FoxPop

Player list ----------------------------------------------------o[ OK ]

Consult player names, number of members--------------o [ OK ]

Exit button---------------------------------------------------o [ OK ]

Add comments in clean and objective correct throughout the code! -------------------------------------------o------------- [ ]

Add and remove name player o--------------------------------- [ ]

Display player names in alphabetical list, with and id number as numeric identification o-------------------------- [ ]

the code! --------------------------------------------------------o [ OK ]

Add and remove name player ---------------------------------o [ OK ]

Display player names in alphabetical list, with and id number as numeric identification ------------o------------- [ ]

Create a window on Windows to display the code o---------- [ ]

Create separate files for (functions / global variables / visual part / index) -----------o [ OK ]

Version 1.0.1 --> 2.1. Registration of Mobs and Events types ////////// [ ]

2.2. Implements for Excel ////////////////////////////// [ ]

2.3 Receive data from a website and store it //////// [ ]

2.4 Create a framework for automated Mob couting [ ]

The entire repository created and managed by the Git terminal. Material "codado" in VScode.

by ("FoxPop _ Fábio Cesar")

    [>> Organograma Moriquendi END <<]

    [Pacote de Funções]
- Conjunto das principais funções criadas puras para o software.

INI --> Todas as funções criadas na pasta --> classMF --> packMF.py
@ Teste --------> Somente para testes rápidos
@ ListaPlayer --> Chama lista de Jogadores cadastrados com id
@ MenuLM -------> --> Menu Cadastro <-- sem interatividade cadastro, remover, buscar, lista, Jogadores
@ Escolha ------> Local para interagir com opções do Menu Principal ( if ).
@ MenuCad ------> Escolhas do @MenuLM ( if )/ MENU cadastro, remover, buscar, lista, Jogadores
@ Menuo --------> --> Menu Principal <-- Parte grafica do menu sem interatividade. Chama automáticamente a função @Escolha <--
FIM <-- Todas as funções criadas em <-- classMF

    [Variável Global]
- Conjunto de variáveis global separado no arquivo --> mfglobal.py / pasta raiz

INI --> Variáveis Global -->
- NomePlayer  --> Lista de jogadores cadastrados
- qt          --> Quantidade de jogadores cadastrados
- contador    --> Quantidade de opções escolhidas "controle dev"
- IdJogador   --> Numeros de 1 a 100 / Referência ID para jogadores cadastrados
FIM <-- Variáveis Global <--

By. ( FoxPop / FabioCesar )
"""
