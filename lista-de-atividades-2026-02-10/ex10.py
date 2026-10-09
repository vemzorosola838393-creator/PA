n = int(input("Quantos números deseja digitar? "))

vetor = []

for i in range(n):
    valor = int(input(f"Digite o valor {i}: "))
    vetor.append(valor)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if vetor[j] > vetor[j + 1]:
            temp = vetor[j]
            vetor[j] = vetor[j + 1]
            vetor[j + 1] = temp

print("Vetor ordenado:", end=" ")

for i in range(n):
    print(vetor[i], end=" ")