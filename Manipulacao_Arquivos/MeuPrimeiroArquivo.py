with open("Primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)