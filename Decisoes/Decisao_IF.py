nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagianete=input("Suspeita de doença infectocontagiosa?").upper()
if idade>=65:
        print("O paciente " + nome + " possui atendimento prioritário!")
elif doenca_infectocontagianete=="SIM":
    print("O paciente " + nome + " deve ser direcionado para a sala de espera reservada.")
else:
    print("O paciente " + nome + " Não possui atendimento prioritário e pode aguardar na sala comum!")
