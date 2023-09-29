import random

print(random.random())

print(random.randrange(1, 100))

print("Par" if random.randrange(1, 100)%2 == 0 else "Impar" )

frutas = ["maçã", "pêra", "uva", "Laranja"]

print(random.choice(frutas))