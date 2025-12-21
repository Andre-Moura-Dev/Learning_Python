soma = 0
numero = 0

while True:
    entrada = input("Informe um número (ou 0 para parar): ")
    
    numero = int(entrada)
    
    if numero == 0:
        break
    soma += numero # Soma e atribui
print(f"A soma dos númeors digitados foi: {soma}")