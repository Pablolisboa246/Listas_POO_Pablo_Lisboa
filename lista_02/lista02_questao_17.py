agenda={}
qtd = int(input("quantos contatos vai cadastrar"))

for i in range(qtd):
    nome=input("digite nome do contato")
    telefone=input("digite telefone")
    agenda[nome]=telefone

busca = input("digite nome pra buscar")

if busca in agenda:
    print("telefone",agenda[busca])
else:
    print("contato nao encontrado")
