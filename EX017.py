import math
cat_opots = float(input("qual o comprimento do cateto oposto?  "))
cat_adj = float(input("qual o comprimento do cateto adjacente? "))
hipotenusa = math.hypot (cat_adj, cat_opots)
print(f"o comprimento da hipotenusa é de : {hipotenusa:.2f}")
