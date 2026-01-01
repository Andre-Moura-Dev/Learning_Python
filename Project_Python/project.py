escolha_usuario = ""

while escolha_usuario != "4":
    print("\n --- MENU SISTEMA ---")
    
    print("\n 1 - Login")
    print("\n 2 - Mostrar Números")
    print("\n 3 - Verificar Idade")
    print("\n 4 - Sair")
    
    escolha_usuario = input("Escolha uma opção: ")
    
    match escolha_usuario:
        case "1":
            senha = ''
            
            while senha != "123":
                senha = input("Informe sua Senha: ")
            print("Login Realizado com sucesso")
        case "2":
            for numero in range(1, 11):
                if numero % 2 == 0:
                    print("Pár", numero)
                else:
                    print("ímpar", numero)
        case "3":
            idade = int(input("Digite Sua Idade: "))
            
            if idade >= 18:
                print("Maior de Idade")
            elif idade >= 16 and idade < 18:
                print("Menor, mas quase adulto")
            else:
                print("Menor de idade")
        case "4":
            print("Encerrando o sistema...")
        case _:
            print("Opção Inválida")