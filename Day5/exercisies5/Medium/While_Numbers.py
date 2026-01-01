numeros = []

while True:
    num = int(input("Informe números (0 para parar): "))
    if num == 0:
        break
    numeros.append(num)
    
if numeros:
    quantidade = len(numeros)
    soma = sum(numeros)
    media = soma / quantidade
    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Média dos números: {media:.2f}")
else:
    print("Nenhum número foi digitado.")