palavra_digitada = input("Digite uma palavra: ")

contador = 0

for caractere in palavra_digitada:
    contador += 1
    
print(f"A palavra '{palavra_digitada}' tem {contador} letras")