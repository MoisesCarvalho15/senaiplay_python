# Menu
print("Projeto Calculadora SenaiPla\n")
print("Menu Principal")
print("[1] - Adição")
print("[2] - Subtração")
print("[3] - Multiplicação")
print("[4] - Divisão")
print("[5] - Potência")
print("[6] - Raiz Quadrada")
print("[7] - Porcentagem")
print("[8] - Fatorial")
print("[9] - Sair")

# Entrada do usuário
while True:
    opcao = int(input("N° da Operação: "))
    
    # Adição
    if opcao == 1:
        print("\n[ADIÇÃO]")
        print("[NOTA] - Digite os números que deseja somar separando-os por espaços. Exemplo: 1 2")
        
        # Entrada do usuário
        numeros = str(input("Números: "))
        
        # Cria uma lista dos números inseridos pelo usuário
        lista_numeros = list(numeros.split(" "))
        
        soma = 0
        
        # Iterando cada número da lista
        for numero in lista_numeros:
            soma += float(numero)
        print(f"Resultado: {soma}\n")

    # Subtração
    elif opcao == 2:
        print("\n[SUBTRAÇÃO]")
        print("[NOTA] - Digite os números separando-os por espaços. Exemplo: 1 2")
        
        # Entrada do usuário
        numeros = str(input("Números: "))
        
        # Cria uma lista dos números inseridos pelo usuário
        lista_numeros = list(numeros.split(" "))
        
        subtracao = float(lista_numeros[0]) # Inicia com o primeiro elemento da lista
        
        # Iterando cada número da lista
        for numero in range(1, len(lista_numeros)):
            subtracao -= float(lista_numeros[numero])
        print(f"Resultado: {subtracao}\n")
        
    # Multiplicação
    elif opcao == 3:
        print("\n[MULTIPLICAÇÃO]")
        print("[NOTA] - Digite os números separando-os por espaços. Exemplo: 1 2")
        
        # Entrada do usuário
        numeros = str(input("Números: "))

        # Cria uma lista dos números inseridos pelo usuário
        lista_numeros = list(numeros.split(" "))
        
        multiplicacao = 1 # inicia a multiplicação com elemento neutro
        
        # Iterando cada número da lista
        for numero in lista_numeros:
            multiplicacao *= float(numero)
        print(f"Resultado: {multiplicacao}\n")
        
    # Divisão
    if opcao == 4:
        print("\n[DIVISÃO]")
        print("[NOTA] - Digite apenas dois números separando-os por espaços. Exemplo: 1 2")
        
        # Entrada do usuário
        numeros = str(input("Números: "))
        
        # Cria uma lista dos números inseridos pelo usuário
        lista_numeros = list(numeros.split(" "))
        
        if float(lista_numeros[0]) == 0:
            print("Não é possível dividir por zero.")
        else:
            divisao = float(lista_numeros[0]) / float(lista_numeros[1])
            resto_divisao = float(lista_numeros[0]) % float(lista_numeros[1])
            print(f"Resultado: {divisao} | Resto da divisão: {resto_divisao}\n")            

    # Potência
    if opcao == 5:
        print("\n[POTÊNCIA]")
        print("[NOTA] - Digite apenas dois números separando-os por espaços. Exemplo: 1 2")
        
        # Entrada do usuário
        numeros = str(input("Números: "))
        
        # Cria uma lista dos números inseridos pelo usuário
        lista_numeros = list(numeros.split(" "))
        
        potencia = int(lista_numeros[0]) ** int(lista_numeros[1])
        print(f"Resultado: {potencia}\n")
        
    
    # Raiz Quadrada
    if opcao == 6:
        print("\n[RAIZ QUADRADA]")
        print("[NOTA] - Digite os números separando-os por espaços. Exemplo: 1 2")
        
        # Entrada do usuário
        numeros = str(input("Números: "))
        
        # Cria uma lista dos números inseridos pelo usuário
        lista_numeros = list(numeros.split(" "))
        lista_raizes = [] # será usada para armazenar os valores das raízes
        
        for numero in lista_numeros:
            lista_raizes.append(int(numero) ** (1/2)) # add o resultado de cada operação na lista
        for num in range(len(lista_numeros)):
            print(f"Raiz quadrada de {lista_numeros[num]}: {lista_raizes[num]}")
        print()
            
    # Porcentagem
    if opcao == 7:
        print("\n[PORCENTAGEM]")
        print("[NOTA] - Digite o percentual e o valor para ser calculado")
        
        # Entrada do usuário
        numeros = str(input("Números: "))
        
        # Criando uma lista através do input do usuário
        lista_numeros = list(numeros.split(" "))
        
        porcentagem = (int(lista_numeros[0]) / 100 )* int(lista_numeros[1])
        print(f"Resultado: {lista_numeros[0]}% de {lista_numeros[1]} = {porcentagem}\n")
        
        
    # Fatorial
    if opcao == 8:
        print(f"[FATORIAL]")
        print("[NOTA] - Digite os número separados por espaço para serem calculados o seu fatorial")
        
        # Entrada do usuário
        numeros = str(input("Números: "))
        
        # Criando uma lista através do input do usuário
        lista_numeros = list(numeros.split(" "))
        lista_fatorias = [] # lista para armazenar o resultado do calculo fatorial
        
        for numero in lista_numeros:
            fatorial = 1
            for i in range(int(numero), 1, -1): # loop se inicia pelo input do usuário e via decrescendo até chegar a 1
                fatorial *= i
            lista_fatorias.append(fatorial ) # Add o resultado fatorial na lista de resultados
            
        # Imprimindo o resultado de cada cálculo fatorial
        for i in range(len(lista_numeros)):
            print(f"O fatorial de {lista_numeros[i]}: {lista_fatorias[i]}")
        print()

    # Sair
    elif opcao == 9:
        print("\nSaindo do programa...")
        break