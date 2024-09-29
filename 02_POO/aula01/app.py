# Criando uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando uma instância da classe
p1 = Pessoa("José", 23)
p2 = Pessoa("Pedro", 20)

# Imprimindo os os valores de cada instância
print(f"{p1.nome} tem {p1.idade} anos.")
print(f"{p2.nome} tem {p2.idade} anos.")