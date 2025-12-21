opcao = input("Digite uma opção: (\n 1 - Ver Saldo \n 2 - Sacar \n 3 - Depositar) \n")

match opcao:
    case "1":
        print("Seu Saldo é 0")
    case "2":
        print("Saque Selecionado")
    case "3":
        print("Depósito Selecionado")
    case _:
        print("Operação Inválida")