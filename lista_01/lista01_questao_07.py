arquivos =5776

if arquivos % 3 == 0:
    print("os arquivos podem ser divididos igualmente")
else:
    print("os arquivos nao podem serem divididos igualmente")
    print ("sobram", arquivos % 3,"arquivos")
