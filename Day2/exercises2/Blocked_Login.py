usuario_input = input("O usuário está bloqueado? (sim/não): ").lower()

usuario_bloqueado = usuario_input == "sim"

if not usuario_bloqueado:
    print("Permitido!")
else:
    print("Negado!")