nomes=[]
enderecos=[]
dds=[]
telefones=[]

continuar_cadastramento="sim"

while continuar_cadastramento=="sim":

 nome=input("digite nome do usuario ")
 endereco=input("digite endereco ")
 dd=input("digite o dd ")
 telefone=input("digite o telefone ")

 nomes.append(nome)
 enderecos.append(endereco)
 dds.append(dd)
 telefones.append(telefone)

 continuar_cadastramento=input("deseja cadastrar mais alguem? digite sim ou não")

for i in range (len(nomes)):
    print ("nome",nomes [i])
    print ("endereco",enderecos [i])
    print ("dd",dds [i])
    print ("telefone",telefones [i])

arquivo=open("agenda.txt","w")

for i in range (len(nomes)):
 arquivo.write("Nome:"+nomes[i]+"\n")
 arquivo.write("Endereco:"+ enderecos[i]+"\n")
 arquivo.write("DD:"+dds[i]+"\n")
 arquivo.write("Telefone:"+telefones[i]+"\n")

 arquivo.write("-----------------------""\n")

arquivo.close()

buscar_usuarios=input("digite o nome do usuario para pesquisa")
achou=False

for i in range(len(nomes)):
 if nomes[i]==buscar_usuarios:
  print("dd",dds[i])
  print("telefone",telefones[i])
  achou=True

if achou== False:
 print ("contato nao encontrado")




























