#EX034
sal = int(input("Qual é o seu salário? "))
if sal >= 1250:
    print(f"Seu salário será de R$ {sal*1.10}")
else:
    print(f"Seu salário será de R$ {sal*1.15}")