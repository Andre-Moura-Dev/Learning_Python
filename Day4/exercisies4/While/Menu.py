escolha_usuario = ''

while escolha_usuario != '3':
    escolha_usuario = input("Escolha uma opção (1 Mostrar números 2 Pedir Senha e 3 Sair): ")
    
    match escolha_usuario:
        case "1":
            for numero in range(1, 6):
                print(numero)
        case "2":
            senha = ''
            
            while senha != "123":
                senha = input("Informe Sua Senha: ")
            print("Senha Correta!")
        case "3":
            print("Saindo")
        case _:
            print("Opção Inválida")