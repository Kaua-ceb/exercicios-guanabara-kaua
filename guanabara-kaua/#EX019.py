#EX019
import random
alun1 = (input("qual nome do aluno 1: "))
alun2 = (input("qual o nome do aluno 2: "))
alun3 = (input("qual o nome do aluno 3: "))
alun4 = (input("qual o nome do aluno 4: "))
lista = [alun1, alun2, alun3, alun4]
premiado = random.choice(lista)
print(premiado)