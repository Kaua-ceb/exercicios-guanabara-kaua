#EX026
frs = str(input("digite uma frase: ")).strip().upper()
print(f"A letra A aparece {frs.count("A")} vezes na frase")
print(f"A primeira letra A apareceu na {frs.find("A")+1} posição ")
print(f"A ultima letra A aparece na posição de número: {frs.rfind("A")+1}")