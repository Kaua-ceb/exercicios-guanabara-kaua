#EX029
veloc = int(input("qual a velocidade do carro? "))
if veloc >= 80:
    print("Você foi multado")
    multa = (veloc-80) *7
    print(f"você vai ter que pagar R${multa}")
else:
  print("Você está dentro do limite de velocidade! Parábens!")