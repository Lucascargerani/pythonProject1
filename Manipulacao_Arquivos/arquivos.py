baseados = []
with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        baseados.append(registro.split(","))

print(baseados)

print(float(baseados[0] [0]) + float(baseados [0] [1]))