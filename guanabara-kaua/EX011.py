"""EX011"""

altura = float(input("digite a altura da parede: "))
largura = float(input("digite a largura da parede: "))
area = largura * altura
tinta = float(area/2.)
print(f"a sua parede tem dimensao de {altura} x {largura} e sua area e de {area}m², para pintar essa parede, voce precisara de {tinta}L de tinta")
