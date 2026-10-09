soma = 0

for i in range(1, 6):
    nota = float(input(f"Digite a nota {i}: "))
    soma = soma + nota

media = soma / 5

print("Média da turma:", media)