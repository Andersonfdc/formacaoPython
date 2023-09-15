lista = ["vermelho", "azul", "vermelho", "preto"]

Quantidade = lista.count("vermelho") #2
print(Quantidade)
print()

linguagens = ["Python", "C", "PHP", "Java"]

lista.extend(linguagens)
print(lista)
print()

lista.reverse()
print(lista)
print()

lista.sort(key=lambda x: len(x))
print(lista)