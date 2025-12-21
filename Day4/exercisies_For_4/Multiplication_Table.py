numero = int(input("Qual Tabuada voce quer ver? (1 a 10): "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")