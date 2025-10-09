#EX031
dist = int(input("Qual a distancia da viagem? "))
if dist <= 200:
    print(f"A passagem custará {dist*0.5}")
else:
    print(f"A passagem custará {dist*0.45}")