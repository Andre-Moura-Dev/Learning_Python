usuario = "admin"
senha = "1234"

usuario_digitado = input("Informe seu usuário: \n")
senha_digitada = input("Informe sua senha: \n")

if usuario_digitado == usuario and senha_digitada == senha:
    print("Permitido")
else:
    print("Negado")