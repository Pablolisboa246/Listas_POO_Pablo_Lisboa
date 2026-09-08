continuar="s"

while continuar == "s":

    print("1 celsius para fahrenheit")
    print("2 fahrenheit para celsius")
    print("3 celsius para kelvin")
    print("4 kelvin para celsius")
    print("5 fahrenheit para kelvin")
    print("6 kelvin para fahrenheit")

    opcao=int(input("digite opcao"))
    temp=float(input("digite temperatura"))

    if opcao == 1:
        res=(temp*9/5)+32
        print("resultado",res)

    elif opcao == 2:
        res=(temp-32)*5/9
        print("resultado",res)

    elif opcao == 3:
        res=temp+273.15
        print("resultado",res)

    elif opcao == 4:
        res=temp-273.15
        print("resultado",res)

    elif opcao == 5:
        res=(temp-32)*5/9+273.15
        print("resultado",res)

    elif opcao == 6:
        res=(temp-273.15)*9/5+32
        print("resultado",res)

    else:
        print("opcao invalda")

    continuar=input("quer fazer outra conversao s ou n").lower()
