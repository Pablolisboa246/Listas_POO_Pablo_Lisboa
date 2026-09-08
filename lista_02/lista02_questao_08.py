notas=[]
aprov = 0

for i in range(10):
    nota=float(input("digite a nota do aluno"))
    notas.append(nota)

for nota in notas:

    if nota >= 7:
        aprov=aprov + 1

print("quantidae de alunos aprovados",aprov)
