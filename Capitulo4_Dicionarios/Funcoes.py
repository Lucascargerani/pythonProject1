def perguntar():
   return input("O que deseja realizar ?\n" +
"<I> - Para Inseri um usúario\n"+
"<P> - Para Pesquisar um usúario\n" +
"<E> - Para Excluir um usúario\n"+
"<L> - Para listar um usúario: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                            input("Digite a última data de acesso: "),
                                                            input("Qual a última estação acessada: ").upper()]

    salvar(dicionario)

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))

def excluir(dicionario):
    login = input("Digite o login do usuário que deseja excluir: ").upper()
    if login in dicionario:
        del dicionario[login]
        salvar(dicionario)  # Atualiza o ficheiro após exclusão
        print(f"Usuário {login} excluído com sucesso!")
    else:
        print("Usuário não encontrado.")

def pesquisar(dicionario):
    login = input("Digite o login do usuário que deseja pesquisar: ").upper()
    if login in dicionario:
        print(f"Informações do usuário {login}: {dicionario[login]}")
    else:
        print("Usuário não encontrado.")

def listar(dicionario):
    if dicionario:
        print("Listando todos os usuários:")
        for login, dados in dicionario.items():
            print(f"{login}: Nome={dados[0]}, Último Acesso={dados[1]}, Estação={dados[2]}")
    else:
        print("Nenhum usuário encontrado.")

def carregar_dados():
    dicionario = {}
    try:
        with open("bd.txt", "r") as arquivo:
            for linha in arquivo:
                chave, dados = linha.strip().split(":")
                dicionario[chave] = dados.split(",")
    except FileNotFoundError:
        print("Ficheiro não encontrado. Um novo será criado ao salvar.")
    return dicionario
