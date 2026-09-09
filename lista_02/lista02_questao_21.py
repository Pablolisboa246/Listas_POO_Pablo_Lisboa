progr=float(input("digite as horas estudadas de programacao "))
banco=float(input("digite as horas estudadas de banco de dados "))
redes=float(input("digite as horas estudadas de redes de computadores "))

carga_horaria_total = progr+banco+redes

if progr < 0 or banco < 0 or redes < 0:
 print (" os valores sao invalidos")

else:
 print ("A carga horaria total eh de: ",carga_horaria_total, "horas")

