"""EX015"""

aluguel = float(input("quantos dias alugados ? "))
km = float(input("quanto kms foram rodados ? "))
dias_valor = aluguel*60
valor_km = km*0.15
valor_pagar = dias_valor + valor_km
print(f"o valor a ser pago será de R$ {valor_pagar}")
