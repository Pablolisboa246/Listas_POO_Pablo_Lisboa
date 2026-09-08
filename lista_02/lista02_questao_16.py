alunos={}
qtd=int(input("digite quantos alunos vai cadastrar"))

for i in range(qtd):

    nome=input("digite nome do estudante")
    nota=float(input("digite a nota final"))
    alunos[nome]=nota

for nome,nota in alunos.items():

    print("nome",nome)
    print("nota",nota)

    if nota >= 7:
        print("aprovado")
    else:
        print ("reprovado")
