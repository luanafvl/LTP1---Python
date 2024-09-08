# Checking if the student is in the class

turma = ('André', 'Fernanda', 'Luiz')

aluno = (input("Digite o nome do aluno: "))

contagem = 0

for i in range(len(turma)):
    if aluno == turma[i]:
        contagem+=1

if contagem != 0:
    print(f"{aluno} está na turma")
else:
    print(f"{aluno} não está na turma")