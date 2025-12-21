nota_1 = int(input("Informe a 1° nota: "))
nota_2 = int(input("Informe a 2° nota: "))
nota_3 = int(input("Informe a 3° nota: "))

media = nota_1 + nota_2 + nota_3 / 3

if media >= 6:
    print(f"Aprovado com {media:.2f}!")
else:
    print(f"Reprovado com {media:.2f}!")