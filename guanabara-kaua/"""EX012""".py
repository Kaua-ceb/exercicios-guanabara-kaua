"""EX012"""

valor = float(input("qual o valor do produto ? R$: "))
desconto = int(input("qual o valor do desconto ?  "))
valor_desc = (valor- valor*desconto/100)
print(valor_desc)
