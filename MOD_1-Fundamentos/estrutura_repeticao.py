text = input("Enter a text: ")
VOWELS = "AEIOU"

for lirics in text:
    if(lirics.upper() in VOWELS):
        print(lirics, end="|")

for number in range(0,51,5): #range(START|incluido,STOP|excluido,STEP|passo)
    print(number, end ="-")      