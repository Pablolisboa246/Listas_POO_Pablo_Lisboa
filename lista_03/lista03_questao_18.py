itens=[]

for i in range(5):

    nome=input("digite nome do equipamento")
    preco=float(input("digite preco"))
    item={
        "nome":nome,
        "preco":preco
    }

    itens.append(item)

caro=itens[0]

for item in itens:

    print ("nome",item["nome"],"preco",item["preco"])

    if item["preco"] > caro["preco"]:
        caro=item

print("equipamento mais caro",caro["nome"])
print("preco",caro["preco"])
