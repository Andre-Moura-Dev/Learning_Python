turno_escolar = input("Informe o seu turno: (M, T, N): ").lower()

if turno_escolar == "M" or turno_escolar == "m":
    print("Bom dia 😀")
elif turno_escolar == "T" or turno_escolar == "t":
    print("Boa Tarde 😑")
elif turno_escolar == "N" or turno_escolar == "n":
    print("Boa Noite 😞")