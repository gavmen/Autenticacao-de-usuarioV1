with open(r'usuario.txt', 'r') as r:
    arquivouser = r
    usuario = arquivouser.read().splitlines()

with open(r'senhas.txt', 'r') as r:
    arquivosenha = r
    senha = arquivosenha.read().splitlines()


def logar():
    usuarioent = input("Insira o Usuário: ")
    for user in usuario:
        if user == usuarioent:
            print("Usuário encontrado!")
            break
        elif user != usuarioent:
            continue
    li = usuario.index(usuarioent)
    senhaent = input("Insira a Senha: ")
    if senha[li] == senhaent:
        print("Autenticação realizada com sucesso!")
    elif senha[li] != senhaent:
        print("Senha inválida!")


logar()
