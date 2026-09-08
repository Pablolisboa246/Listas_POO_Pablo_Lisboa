frase=input("digite uma frase")
palavras=frase.lower().split()
cont={}

for palavra in palavras:

    if palavra in cont:
        cont[palavra]=cont[palavra]+1
    else:
        cont[palavra]=1

for palavra,quantidade in cont.items():
    print(palavra,":",quantidade)
