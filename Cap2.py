
#    [Cap2 (Exercícios)]
import os
import sys
os.system("cls")
print("Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.")
exer1 = [1,2,3,4,5,6,7,8,9,10]
print(exer1)

print("\nExercício 2 - Crie uma lista de 5 objetos e imprima na tela")
exer2 = ["objeto1","objeto2","objeto3","objeto4","objeto5"]
print(exer2)

print("\nExercício 3 - Crie duas strings e concatene as duas em uma terceira string")
corpo1 = "Corpo1"
corpo2 = "Corpo2"
corpo3 = [corpo1, corpo2]
print(corpo3)
print("\nExercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do objeto tupla para verificar quantas vezes o número 4 aparece na tupla")
tp = (1, 2, 2, 3, 4, 4, 4, 5)
tt = tp.count(4)
print("\nNumero 4 apareceu:",tt,"x")

print("Exercício 5 - Crie um dicionário vazio e imprima na tela")
dc = {}
print(dc)

print("Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela")
dc1 = {"Chave1":10,"Chave2":20,"Chave3":30}
print(dc1)
dc123 = {"Chave1",10,"Chave2",20,"Chave3",30}
print("Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela")
dc111 ={"Chave4":40}
dc1.update({"Chave5":50})
dc1.update(dc111)
print(dc123)

print("\nExercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. Imprima o dicionário na tela.")
dc999 = {"Arquivo1":"Arquivo2","Arquivo3":3,4:5}
print(dc999)

print("\nExercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string")
print("o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e")
print("o quarto elemento um valor do tipo float.")
print("Imprima a lista na tela.\n")
lt4 =["Prim1Elem.",("Tupla1","tupla2"),{"chave1":2,"chave2":4},5.44]
print(lt4)
print("\nExercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.")
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[1:18])