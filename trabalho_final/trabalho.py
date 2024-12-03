import sqlite3

# Falta lidar com o texto do departamento ao criar funcionario

# Conectando com o Banco de Dados
con = sqlite3.connect("tutorial.db")
cur = con.cursor()


'''

INCLUIR ESTA PARTE DO CÓDIGO APENAS NA PRIMEIRA EXECUÇÃO

ONLY INCLUDE THIS PART ON FIRST EXECUTION


cur.execute("CREATE TABLE tb_departamento ("
    "cd_departamento integer primary key autoincrement,"
    "departamento CHAR(45) not null);")

cur.execute("CREATE TABLE tb_funcionario ("
    "matricula integer primary key autoincrement,"
    "funcionario CHAR(45) not null,"
    "cargo CHAR(45) not null,"
    "salario FLOAT not null,"
    "cd_departamento int,"
    "foreign key (cd_departamento) references tb_departamento(cd_departamento));")

'''


class Funcionario:
    def addFuncionario(self):
        print("Adicionando funcionário...")
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        salario = float(input("Salario: "))
        departamento = input("Departamento: ")

        # Verificando se existe algum departamento para o funcionario ser alocado
        isInDepartamentos = False
        for departamentos in cur.execute("SELECT departamento FROM tb_departamento"):
            if departamento == departamentos[0]:
                isInDepartamentos = True

        # Apenas ocorre se já houver um departamento
        if isInDepartamentos:
            cur.execute("INSERT INTO tb_funcionario (funcionario, cargo, salario, departamento) VALUES(?, ?, ?, ?)",
                        (nome, cargo, salario, departamento))
            print(f"Funcionário(a) {nome} adicionado(a).")
        else:
            print("Departamento inválido. Funcionário não adicionado.")

    def editarFuncionario(self):
        print("Editando funcionário...")
        for nomes in cur.execute("SELECT funcionario FROM tb_funcionario"):
            print(nomes)
        comparaNome = input("Funcionário: ")

        # Verifica se o funcionario informado existe
        isInNomes = False
        for nomes in cur.execute("SELECT funcionario FROM tb_funcionario"):
            if comparaNome == nomes[0]:
                isInNomes = True

        if isInNomes:
            print("Novos dados...")
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = float(input("Salario: "))
            departamento = input("Departamento: ")

            isInDepartamento = False
            for i in cur.execute("SELECT departamento FROM tb_departamento"):
                if departamento == i[0]:
                    isInDepartamento = True

            if isInDepartamento:
                cur.execute("UPDATE tb_funcionario SET funcionario = ?, cargo = ?, salario = ?, departamento = ? WHERE funcionario = ?",
                            (nome, cargo, salario, departamento, comparaNome))
                print(f"Funcionário(a) {nome} alterado(a).")
            else:
                print("Departamento inválido. Dados não alterados.")
        else:
            print("Funcionário inválido. Dados não alterados.")

    def removerFuncionario(self):
        print("Removendo Funcionário...")
        for nomes in cur.execute("SELECT funcionario FROM tb_funcionario"):
            print(nomes)
        comparaNome = input("Funcionário: ")

        isInNomes = False
        for nomes in cur.execute("SELECT funcionario FROM tb_funcionario"):
            if comparaNome == nomes[0]:
                isInNomes = True

        if isInNomes:
            cur.execute("DELETE FROM tb_funcionario WHERE funcionario = ?", (comparaNome,))
            print(f"Funcionário(a) {comparaNome} removido(a).")
        else:
            print("Funcionário inválido.")

class Departamento:
    def addDepartamento(self):
        print("Adicionando departamento...")
        nome = input("Nome: ")

        # Verificando se o departamento já existe
        isInDepartamentos = False
        for departamentos in cur.execute("SELECT departamento FROM tb_departamento"):
            if nome == departamentos[0]:
                isInDepartamentos = True

        if isInDepartamentos:
            print("Impossível adicionar departamento já existente.")
        else:
            cur.execute("INSERT INTO tb_departamento (departamento) VALUES (?)", (nome,))
            print(f"Departamento {nome} adicionado(a).")

    def editarDepartamento(self):
        print("Editando departamento...")
        for nomes in cur.execute("SELECT departamento FROM tb_departamento"):
            print(nomes)
        comparaNome = input("Departamento: ")

        isInDepartamentos = False
        for nomes in cur.execute("SELECT departamento FROM tb_departamento"):
            if comparaNome == nomes[0]:
                isInDepartamentos = True

        if isInDepartamentos:
            print("Novos dados...")
            nome = input("Nome: ")
            cur.execute("UPDATE tb_departamento SET departamento = ? WHERE departamento = ?", (nome, comparaNome))
            print(f"Departamento alterado.\nAntigo: {comparaNome}\nNovo: {nome}")
        else:
            print("Departamento inválido. Dados não alterados.")

    def removerDepartamento(self):
        print("Removendo departamento...")
        for departamentos in cur.execute("SELECT departamento FROM tb_departamento"):
            print(departamentos)
        comparaNome = input("Departamento: ")

        isInNomes = False
        for departamentos in cur.execute("SELECT departamento FROM tb_departamento"):
            if comparaNome == departamentos[0]:
                isInNomes = True

        if isInNomes:
            cur.execute("DELETE FROM tb_departamento WHERE departamento = ?", (comparaNome,))
            print(f"Departamento {comparaNome} removido(a).")
        else:
            print("Departamento inválido.")

# Inicializando
funcionario = Funcionario()
departamento = Departamento()

# Menu principal
print("Bem-vindo(a) à minhaEmpresa!")
gerenciar = 0
while gerenciar != 3:
    gerenciar = int(input("(1) - Gerenciar Funcionários\n(2) - Gerenciar Departamentos\n(3) - Sair\n"))
    if gerenciar == 1:
        print("Gerenciando funcionários...")
        opt = 0
        while opt != 4:
            opt = int(input("(1) - Adicionar Funcionário\n(2) - Editar Funcionário\n(3) - Remover Funcionário\n(4) - Voltar\n"))
            if opt == 1:
                funcionario.addFuncionario()
            elif opt == 2:
                funcionario.editarFuncionario()
            elif opt == 3:
                funcionario.removerFuncionario()

    elif gerenciar == 2:
        print("Gerenciando departamentos...")
        opt = 0
        while opt != 5:
            opt = int(input("(1) - Adicionar Departamento\n(2) - Editar Departamento\n(3) - Remover Departamento\n(4) - Mostrar Departamentos\n(5) - Sair\n"))
            if opt == 1:
                departamento.addDepartamento()
            elif opt == 2:
                departamento.editarDepartamento()
            elif opt == 3:
                departamento.removerDepartamento()
            elif opt == 4:
                for i in cur.execute("SELECT departamento FROM tb_departamento"):
                    print(i)
    elif gerenciar == 3:
        print("Até logo!")
    else:
        print("Opção inválida.")
