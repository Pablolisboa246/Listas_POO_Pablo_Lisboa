aluno={}
aluno["nome"] = input("digite nome")
aluno["matricula"]=input("digite matricula")
aluno["idade"] = int(input("digite idade"))
aluno["curso"]=input("digite curso")
aluno["semestre"] = int(input("digite semestre"))
aluno["semestre"]=int(input("digite o semestre novo"))
aluno["email"]=input("digite email institucional")

del aluno["idade"]

print("dicionario atualizdo")
print (aluno)
