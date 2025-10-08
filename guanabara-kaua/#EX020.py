#EX020
import random
ualun = (input("qual o primeiro aluno?: "))
dalun = (input("qual o segundo aluno?: "))
talun = (input("qual o terceiro aluno?: "))
qalun = (input("qual o quarto aluno?: "))
lista = [ualun, dalun, talun, qalun]
random.shuffle(lista)
print(f"a ordem da lista vai ser {lista}")