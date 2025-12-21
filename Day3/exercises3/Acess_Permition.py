idade = int(input("Informe sua idade: \n"))
autorizacao_input = input("Tem Autorização Acesso? (sim/não): ").lower()

autorizacao_acesso = autorizacao_input == "sim"

match autorizacao_acesso:
    case True if idade >= 18:
        print("Acesso liberado")
    case True if idade < 18 and autorizacao_acesso:
        print("Acesso liberado mas, com autorização")
    case _:
        print("Acesso Negado")