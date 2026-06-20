assentos_ocupados = []

LINHAS = 10
COLUNAS = 10

while True:
    print("\n --- CINEMA ---")
    print("1 - Ver assentos")
    print("2 - Reservar")
    print("3 - Cancelar")
    print("4 - Ver Ocupados")
    print("5 - Sair")
    
    opcao = input("Escolha a opção: ")
    
    match opcao:
        case "1":
            print("\n --- ASSENTOS ---")
            
            for linha in range(1, LINHAS + 1):
                for coluna in range(1, COLUNAS + 1):
                    
                    tuplaLugar = (linha, coluna)
                    
                    if linha in assentos_ocupados:
                        print("[X]", end=" ")
                    else:
                        print("[ ]", end=" ")
                
                print()
        case "2":
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            
            tuplaLugar = (linha, coluna)
            
            if tuplaLugar in assentos_ocupados:
                print("Lugar Ocupado!")
            else:
                assentos_ocupados.append(tuplaLugar)
                print("Reserva Feita!")
        case "3":
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            
            tuplaLugar = (linha, coluna)
            
            if tuplaLugar in assentos_ocupados:
                assentos_ocupados.remove(tuplaLugar)
                print("Reserva Cancelada!")
            else:
                print("Esse lugar não está reservado!") 
        case "4":
            print("\n --- Assentos Ocupados")
            
            for lugar in assentos_ocupados:
                print(tuplaLugar)
        case "5":
            print("Saindo do Sistema...")
            break
        case _:
            print("Opção Inválida!")