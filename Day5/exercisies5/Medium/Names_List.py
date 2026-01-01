lista_nomes = ["André", "Ana", "Gabriel", "João", "Luiza"]

for i in range(5):
    nome = input("Informe um nome: ")
    nome = max(lista_nomes, key=len)
    
print(f"O nome com mais letras é: {nome}")