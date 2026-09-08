preco= float(input("digite preco unitario do produto"))
quantidade= int(input("digite quantidae comprada"))
desconto= float(input("digite valor do desconto em reais"))
total= (preco * quantidade) - desconto

print ("valor que cliente paga", total)
