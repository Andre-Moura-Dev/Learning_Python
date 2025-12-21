# Sair do Loop quando x for banana
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
    
    if x == "banana":
        break


# A interrupção acontece depois da validação
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        break
    print(x)