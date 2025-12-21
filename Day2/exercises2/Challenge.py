idade = int(input("Digite a sua idade: "))
autorizacao_input = input("Tem autorização? (sim/não): ").lower()

autorizacao_pais = autorizacao_input == "sim"

if idade >= 18:
    print("Entrada Permitida")
elif idade < 18 and autorizacao_pais:
    print("Entrada Permitida mas, com autorização")
else:
    print("Entrada Negada")