# Lista interativa

nomes = []

while True:
    nome = input("Digite um nome para adicionar na lista: ")
    nomes.append(nome) # adicionando o nome digitado na lista
    sair = str(input("Deseja sair [s] [n]? ")).lower()
    if sair == "s":
        print(f"Nomes salvos na lista: {nomes}")
        break