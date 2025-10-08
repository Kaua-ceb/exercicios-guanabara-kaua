#EX023
num = int(input("digite um numero: "))
print(f"analisando o numero {num}...")
u = num// 1 % 10
d = num// 10 % 10
c = num// 100 % 10
m = num// 1000 % 10
print(f"A sua unidade corresponde á {u}")
print(f"A sua dezena corresponde á {d} ")
print(f"A sua centena corresponde á {c}")
print(f"O seu milhar corresponde á {m}")
