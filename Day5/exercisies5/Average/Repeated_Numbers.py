numeros = [2, 5, 2, 8, 2, 9, 5]

print("Números que aparecem mais de 1 vez:\n")

for numero in set(numeros):
    quantidade = numeros.count(numero)
    
    if quantidade > 1:
        print(f"O número {numero} aparece {quantidade} vezes")