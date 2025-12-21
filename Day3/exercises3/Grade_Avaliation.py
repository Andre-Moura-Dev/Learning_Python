nota_aluno = int(input("Informe uma nota (0 a 10): "))

match nota_aluno:
    case True if nota_aluno >= 7:
        print("Aprovado")
    case True if nota_aluno >= 5 and nota_aluno < 7:
        print("Recuperação")
    case True if nota_aluno < 5:
        print("Reprovado")
    case _:
        print("Nota Inválida")