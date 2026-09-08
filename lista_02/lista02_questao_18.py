inv={}
qtd=int(input("quantos equipamentos vai cadastrar"))

for i in range(qtd):
    pat=input("digite o patrimonio")
    equip=input("digite equipamento")
    marca =input("digite marca")
    situacao=input("digite situacao")
    inv[pat]={
        "equipamento":equip,
        "marca":marca,
        "situacao":situacao
    }

for pat,info in inv.items():

    print("patrimonio",pat)

    for chave,valor in info.items():
        print(chave,valor)
