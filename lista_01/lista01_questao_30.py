nota= float(input("digite nota final"))

if nota < 0 or nota > 10:
    print ("nota invalda")

elif nota >= 7:

    print ("aprovado")
elif nota >= 5:

    print ("recuperacao")

else:
    print ("reprovado")
