nome = input("digite nome do participante")
ano_nascimento = int(input("digite ano de nascimento"))
ano_atual = 2026
idade = ano_atual - ano_nascimento

if idade >= 18:

    print (nome, "tem", idade, "anos e pode entra desacompanhado")

else:
    print(nome, "tem", idade, "anos e precisa ta acompanhado")
