usuario_input = input("O usuário está bloqueado? (sim/não): ").lower()

usuario_bloqueado = usuario_input == "sim"

match True:
    case True if not usuario_bloqueado:
        print("Permitido!")
    case True if usuario_bloqueado:
        print("Negado!")