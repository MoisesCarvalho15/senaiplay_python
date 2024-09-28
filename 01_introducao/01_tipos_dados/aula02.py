# Entrada de dados
nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")

# Imprimindo as variáveis e seus tipos
print(nome, type(nome))
print(idade, type(idade))
print()

# Convertendo  o valor da entrada já obtido
idade = int(idade)
print(idade, type(idade))

# Convertendo diretamente na entrada do dado
idade2 = int(input("Digite sua idade: "))
print(idade2, type(idade2))

# Formatação de strings
print(f"{nome} tem {idade} anos e está cursando o curso de Introdução a programação com Python.")