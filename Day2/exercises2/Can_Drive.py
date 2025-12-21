idade = int(input("Informe sua idade: "))
carteira_input = input("Tem Carteira? (sim/não): ").lower()

tem_carteira = carteira_input == "sim"

if idade >= 18 and tem_carteira:
    print("Pode Dirigir!")
else:
    print("Não pode dirigir!")