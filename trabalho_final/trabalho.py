import sqlite3


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

        print("Departamentos disponíveis:")
        for departamentos in cur.execute("SELECT cd_departamento, departamento FROM tb_departamento"):
            print( f"{departamentos[0]} - {departamentos[1]}", end=";\n")

        departamento = input("Código do departamento: ")

        # Verificando se existe algum departamento para o funcionario ser alocado
        isInDepartamentos = False
        for departamentos in cur.execute("SELECT cd_departamento FROM tb_departamento"):
            if int(departamento) == departamentos[0]:
                isInDepartamentos = True

        # Apenas ocorre se já houver um departamento
        if isInDepartamentos:
            cur.execute("INSERT INTO tb_funcionario (funcionario, cargo, salario, cd_departamento) VALUES(?, ?, ?, ?)",
                        (nome, cargo, salario, departamento))
            print(f"Funcionário(a) {nome} adicionado(a).")
        else:
            print("Departamento inválido. Funcionário não adicionado.")

    def editarFuncionario(self):

        # Verifica se existe algum funcionário
        cur.execute("SELECT funcionario FROM tb_funcionario")
        funcionarios = cur.fetchall()
        if not funcionarios:
            print("Não há funcionários na empresa.\n")
            return

        # Se existir, o código funciona normalmente
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

            print("Departamentos disponíveis:")
            for departamentos in cur.execute("SELECT cd_departamento, departamento FROM tb_departamento"):
                print(f"{departamentos[0]} - {departamentos[1]}", end=";\n")

            departamento = input("Código do departamento: ")

            # Verificando se existe algum departamento para o funcionario ser alocado
            isInDepartamentos = False
            for departamentos in cur.execute("SELECT cd_departamento FROM tb_departamento"):
                if int(departamento) == departamentos[0]:
                    isInDepartamentos = True

            if isInDepartamentos:
                cur.execute("UPDATE tb_funcionario SET funcionario = ?, cargo = ?, salario = ?, cd_departamento = ? WHERE funcionario = ?",
                            (nome, cargo, salario, departamento, comparaNome))
                print(f"Funcionário(a) {nome} alterado(a).")
            else:
                print("Departamento inválido. Dados não alterados.")
        else:
            print("Funcionário inválido. Dados não alterados.")

    def removerFuncionario(self):
        cur.execute("SELECT funcionario FROM tb_funcionario")
        funcionarios = cur.fetchall()
        if not funcionarios:
            print("Não há funcionários na empresa.\n")
            return

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


    def mostrarFuncionarios(self):
        cur.execute("SELECT funcionario FROM tb_funcionario")
        funcionarios = cur.fetchall()
        if not funcionarios:
            print("Não há funcionários na empresa.\n")
            return

        print("Funcionario - Departamento")
        cur.execute("SELECT f.funcionario, d.departamento FROM tb_funcionario f JOIN tb_departamento d ON f.cd_departamento = d.cd_departamento")
        for funcionario in cur.fetchall():
            print(f"{funcionario[0]} - {funcionario[1]}")




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
            print(f"Departamento {nome} adicionado.")

    def editarDepartamento(self):
        cur.execute("SELECT departamento FROM tb_departamento")
        departamentos = cur.fetchall()
        if not departamentos:
            print("Não há departamentos na empresa.\n")
            return

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
        cur.execute("SELECT departamento FROM tb_departamento")
        departamentos = cur.fetchall()
        if not departamentos:
            print("Não há departamentos na empresa.\n")
            return

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
            print(f"Departamento {comparaNome} removido.")
        else:
            print("Departamento inválido.")


    def mostrarDepartamentos(self):
        cur.execute("SELECT departamento FROM tb_departamento")
        departamentos = cur.fetchall()
        if not departamentos:
            print("Não há departamentos na empresa.\n")
            return
        for departamento in cur.execute("SELECT departamento FROM tb_departamento"):
            print(departamento)


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
        while opt != 5:
            opt = int(input("(1) - Adicionar Funcionário\n(2) - Editar Funcionário\n(3) - Remover Funcionário\n(4) - Mostrar funcionários\n(5) - Voltar\n"))
            if opt == 1:
                funcionario.addFuncionario()
            elif opt == 2:
                funcionario.editarFuncionario()
            elif opt == 3:
                funcionario.removerFuncionario()
            elif opt == 4:
                funcionario.mostrarFuncionarios()

    elif gerenciar == 2:
        print("Gerenciando departamentos...")
        opt = 0
        while opt != 5:
            opt = int(input("(1) - Adicionar Departamento\n(2) - Editar Departamento\n(3) - Remover Departamento\n(4) - Mostrar Departamentos\n(5) - Voltar\n"))
            if opt == 1:
                departamento.addDepartamento()
            elif opt == 2:
                departamento.editarDepartamento()
            elif opt == 3:
                departamento.removerDepartamento()
            elif opt == 4:
                departamento.mostrarDepartamentos()
    elif gerenciar == 3:
        print("Até logo!")
    else:
        print("Opção inválida.")

'''
Usar apenas se quiser salvar as alterações no BD
con.commit()
'''

con.close()
