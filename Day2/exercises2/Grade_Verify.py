nota_aluno = int(input("Digite a nota do aluno (0 a 10): "))

if nota_aluno >= 7:
    print("Aprovado!")
elif nota_aluno >= 5 and nota_aluno < 7:
    print("Recuperação")
else:
    print("Reprovado")