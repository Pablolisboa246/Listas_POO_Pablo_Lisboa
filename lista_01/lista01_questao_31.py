ano =int(input("digite ano"))

if ano % 400 == 0:

    print("ano eh bissexto")
elif ano % 4 == 0 and ano % 100 != 0:

    print("ano eh bissexto")

else:
    print("ano nao eh bissexto")
