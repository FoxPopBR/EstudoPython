# -*- coding: utf-8 -*-

"""
#1.Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.   

idade = int(input("Digite sua idade: "))
 
if idade >= 18:
    print("Maior de idade")
elif idade < 18:
    print("Menor de idade")
"""


"""
#2. Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
 
media = (nota1+nota2)/2
 
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
"""



"""
#3. Escreva um programa que resolva uma equação de segundo grau.   

from math import sqrt
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
 
delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)
 
if raiz_delta < 0:
    print("Delta negativo")
else:
    x1 = (-b + raiz_delta)/2*a
    x2 = (-b + raiz_delta)/2*a
 
    print("As raízes são", x1, "e", x2)


#4. Escreva um programa que ordene uma lista numérica com três elementos.   

lista = [3,2,1]
print(sorted(lista))
"""


"""
#5. Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   

n1 = int(input("Digite o primeiro número: "))
sinal = input("Digite o sinal: ")
n2 = int(input("Digite o segundo número: "))
 
if sinal == "+":
    op = n1 + n2
 
elif sinal == "-":
    op = n1 - n2
 
elif sinal == "/":
    op = n1 + n2
 
elif sinal == "*":
    op = n1 * n2
 
else:
    print("Sinal inválido.")
 
print(op)
"""



"""
a = 2
b = 0
c = ""
try:
    print(a/b)
   
except:
    print("não deu")

#isso para não parar a execução do código em um error
"""



"""
import random

numero = random.randint(0, 100)
number = [2,5,7,123,6,88,1,23,5,0]
nb = random.choice(number)

print (nb)
"""

"""
lista1 = [1,2,3,4,5,6]
lista2 = ["Hi","Hello","Bye","TKS","GG"]
lista3 = [0,"Não","Zica","TMJ",9.13,True,False]

#for i in lista1:
 #   print(i)

for x in range (0,10,3):

    print (x)

"""






"""

x = 1
z = "fim terminou"
while x < 20:
    print (x)
    x = x+1
  
print (x,z,"teste aqui")

"""
