notas = [6.3, 7.5, 9.2, 5.1, 6.8]

soma = 0
contagem = 0

for i in notas:
    soma += notas[i]
    if notas[i] >= 6:
        contagem += 1

media = soma / len(notas)

print(f"Média da turma: {media:.2f}\n")
print(f"Quantidade de notas acima da média: {contagem}")
