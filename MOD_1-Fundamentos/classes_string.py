name = "pYtHoN"

print(name.upper())  # maiúsculo
print(name.lower())  # minúsculo
print(name.title())  # primeira letra maiúscula

name = "     Python"

print(name.strip())  # Remove espeços da direita e esquerda
print(name.lstrip())  # Remove espeços da esquerda
print(name.rstrip())  # Remove espeços da direita

menseger = f''' 
 lorenipsu lorenipsu lorenipsu
 lorenipsu
 lorenipsu lorenipsu
'''
print(menseger)

# imprime a letra na posição informada
part_name = "Python"
print(part_name[0])

# verifica se a palavra existe na frase
frase = "O rato roeu a roupa do rei de roma"

if "rato" in frase:
    print("Existe")