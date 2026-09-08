quadrados = {}

for numero in range(1,11):
    quadrados[numero]=numero**2

for numero,quadrado in quadrados.items():
    print(numero,quadrado)
