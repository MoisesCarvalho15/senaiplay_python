# Criando uma lista
nomes = ["Moisés", "Carlos", "Maria", "Gustavo"]

# Tamanho da lista
print(f"A lista de nomes tem {len(nomes)} nomes.")

"""
- Acessando um determinado elemento da lista.
- Elementos de listas podem ser acessadas através de seu índice.
- Começando a partir do número zero.
"""
print(f"O terceiro nome da lista é: {nomes[2]}\n")

# Inserindo elementos na lista passando o índice
print(f"Lista de nomes antes do insert: {nomes}\n")
nomes.insert(2, "Ricardo")
print(f"Listas de nomes depois do insert: {nomes}\n")

# Embaralhando os elementos da lista
print(f"ista normal: {nomes}")
import random
random.shuffle(nomes)
print(f"Lista embaralhada: {nomes}")

# Ordenando a lista
nomes.sort()
print(f"\nNomes em ordem: {nomes}")

# Removendo um elemento através de seu índice
nomes.pop(1)
print(f"\nLista atualizada: {nomes}")

# Esvaziando a lista
nomes.clear()
print(f"Nomes na lista: {nomes}")