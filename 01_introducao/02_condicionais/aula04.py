"""
# Operadores lógicos
- and (retorna TRUE quando todas as condições forem verdeiras)
- or (retorna TRUE com apenas uma condição sendo verdeira)
- not (inverte o resultado da condição. Se for TRUE, vira False e vice-versa)
"""

# Pegando a entrada do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Condicional com if, elif and else
if num1 > num2 and num1 > num3:
    print(f"O número {num1} é maior que os outros números.")
elif num2 > num1 and num2 > num3:
    print(f"O número {num2} é maior que os outros números.")
elif num3 > num1 and num3 > num2:
    print(f"O número {num3} é maior que os outros números.")
else:
    print(f"Os números são iguais!")
