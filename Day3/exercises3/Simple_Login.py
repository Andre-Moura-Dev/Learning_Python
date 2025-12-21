usuario = "admin"
senha = "123"

usuario_digitado = input("Digite o seu usuário: ")
senha_digitada = input("Digite su senha: ")

match True:
    case True if usuario_digitado == usuario and senha_digitada == senha:
        print("Login Bem sucedido")
    case True if usuario_digitado == usuario and senha_digitada != senha:
        print("Senha Incorreta")
    case _:
        print("Usuário não encontrado")