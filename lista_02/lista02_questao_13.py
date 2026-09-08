disciplina={
    "nome":"poo",
    "professor":"professor",
    "carga_horaria":60,
    "periodo":2
}

chave = input("digite o nome de uma chave")

if chave in disciplina:
    print("a chave existe e foi encontrada")
else:
    print ("a chave nao foi encontrada")
