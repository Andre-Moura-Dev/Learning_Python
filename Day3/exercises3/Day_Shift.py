turno_dia = input("Informe o turno do dia (M, T, N): ").lower()

match turno_dia:
    case "M" | "m":
        print("Bom dia")
    case "T" | "t":
        print("Boa Tarde")
    case "N" | "n":
        print("Boa Noite")
    case _:
        print("Turno Inválido")