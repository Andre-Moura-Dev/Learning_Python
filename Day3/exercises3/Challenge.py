escolhas_menu = input("Escolha uma opção abaixo: (\n 1 - Login, \n 2 - Cadastro, \n 3 - Sair \n): ")

match escolhas_menu:
    case "1":
        usuario = input("Informe seu usuário: \n")
        senha = input("Informe sua senha: \n")
        
        if usuario == "admin" and senha == "123":
            print("Permissão Concedida")
        else:
            print("Permissão Negada")
    case "2":
        print("Cadastro em construção")
    case "3":
        print("Saindo do sistema")
    case _:
        print("Opção Inválida")