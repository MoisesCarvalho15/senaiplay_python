# For range
for i in range(1, 5):
    print(i, "- Olá")
    
print() # linha vazia

# Iterando números 2 em 2
for i in range(0, 11, 2):
    print(i)
    
print() # linha vazia

# while - Executa um código até que a condição seja atendida
cont = 1
while cont <= 5:
    print("Olá")
    cont += 1

    
# while break - Finaliza o programa quando aquela condição for atendida
while True:
    print("\nOlá")
    if input("Deseja finalizar o programa? ") == "s" or "sim":
        break