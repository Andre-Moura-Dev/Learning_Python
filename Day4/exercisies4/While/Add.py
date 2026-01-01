soma = 0
numero = 0

while True:
    entrada = input("Digite números para somar (ou 0 para parar): ")
    
    numero = int(entrada)
    
    if numero == 0:
        break
    soma += numero
print(f"A Soma dos números digitados foi: {soma}")