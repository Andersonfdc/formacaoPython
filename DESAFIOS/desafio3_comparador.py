N = int(input())

for _ in range(N):
    A, B = input().split()  # Lê os valores A e B separados por espaço
    if A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")
