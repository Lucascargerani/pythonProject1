#
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  seriais.append(int(input("Número Serial: ")))
  departamentos.append(input("Departamento: "))
  resposta = input("Digite S para continuar: ").upper()

#
for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])

#
busca=input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
  if busca==equipamentos[indice]:
    print("Valor..: ", valores[indice])
    print("Serial.:", seriais[indice])

# Como podemos observar no código acima, quando igualamos uma lista (acompanhada de um índice), sobrescrevemos o conteúdo do dado na posição especificada pelo índice, ou seja:
# departamentos[0]=”Teste” => essa linha seria responsável por substituir pela string “Teste” o dado que está na posição zero.
depreciacao = input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0, len(equipamentos)):
        if depreciacao == equipamentos[indice]:
            print("Valor antigo: ", valores[indice])
            valores[indice] = valores[indice] * 0.9
            print("Novo valor: ", valores[indice])

# Com esses exemplos, você aprendeu a pesquisar um dado dentro de uma lista e também a excluir um elemento específico dentro de uma lista.
serial=int(input("Digite o serial do equipamento que será excluido: "))
for indice in range(0, len(departamentos)):
  if seriais[indice]==serial:
    del departamentos[indice]
    del equipamentos[indice]
    del seriais[indice]
    del valores[indice]
    break

for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])