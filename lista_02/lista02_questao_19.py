alunos={}
qtd=int(input("digite a quantidae de alunos"))

for i in range(qtd):
    nome=input("digite nome do aluno")
    nota1=float(input("digite nota 1"))
    nota2=float(input("digite nota 2"))
    med=(nota1+nota2)/2
    alunos[nome]={
        "nota 1":nota1,
        "nota 2":nota2,
        "media":med
    }

for nome,info in alunos.items():

    print("aluno",nome)
    print("nota 1",info["nota 1"])
    print("nota 2",info["nota 2"])
    print("media",info["media"])

    if info["media"] >= 7:
        print("situacao aprovado")
    else:
        print("situacao reprovado")
