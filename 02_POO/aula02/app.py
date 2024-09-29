class Forma:
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, baseP, alturaP):
        self.base = baseP
        self.altura = alturaP
    
    def calcular_area(self):
        return self.base * self.altura
    
class Circulo(Forma):
    def __init__(self, raioP):
        self.raio = raioP
    
    def calcular_area(self):
        return 3.14 * self.raio ** 2
    
ret = Retangulo(5, 3)
print(f"Retângulo: {ret.calcular_area()}")

circ = Circulo(4)
print(f"Círculo: {circ.calcular_area()}")
