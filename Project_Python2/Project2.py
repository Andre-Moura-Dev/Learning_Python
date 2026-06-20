alunos = []

while True:
    print("\n --- MENU ---")
    print("1 - Cadastrar aluno")
    print("2 - Listar aluno")
    print("3 - Buscar aluno")
    print("4 - Remover aluno")
    print("5 - Sair")
    
    opcao = input("Escolha uma das opções abaixo: ")
    
    match opcao:
        case "1":
            nome = input("Informe seu nome: \n")
            idade = int(input("Informe sua idade: \n"))
            
            if nome.strip() == "":
                print("Nome não pode ser vazio!")
                continue
            
            if idade < 0:
                print("Idade inválida!")
            
            tuplaAlunos = (nome, idade)
            
            alunos.append(tuplaAlunos)
            
            print("Aluno Cadastrado com Sucesso!")
        case "2":
            for indice, aluno in enumerate(alunos):
                print(f"{indice + 1}º Aluno: {aluno}")
        case "3":
            nome_aluno = input("Informe o nome que deseja procurar: ").lower()
            encontrado = False
            
            for nome, idade in alunos:
                if nome.lower() == nome_aluno:
                    print(f"O aluno com {nome} foi encontrado com idade {idade}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"O nome '{nome_aluno}' não existe na lista")
            
        case "4":
            print("Lista de Alunos:")
            for i, aluno in enumerate(alunos):
                print(f"{i}: {aluno}")
                
            indice = int(input("\n Informe o número (indice) do aluno que deseja remover: "))
            
            aluno_removido = alunos.pop(indice)
            print(f"\n Aluno '{aluno_removido}' removido com sucesso!")
            print("Lista Atualizada: ", alunos)
        case "5":
            print("Saindo...")
            break
        case _:
            print("Opção Inválida")