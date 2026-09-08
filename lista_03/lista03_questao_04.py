programas=["chrome","vscode","python","git","firefox"]

print ("lista original",programas)

novo=input("digite nome do software novo")
programas.append(novo)

programas.pop(1)

print("lista depois da alteracao",programas)
