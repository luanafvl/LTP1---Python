class ContaBancaria:
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, saldo):
        pass

    def sacar(self, saldo):
        pass

    def calcularSaldo(self):
        pass

    def mostrarDados(self, numero, nome, saldo):
        print("Número da conta: " + numero)
        print("Nome: " + nome)
        print("Saldo: R$", saldo, "\n")


class ContaCorrente(ContaBancaria):

    def __init__(self, numero, titular, saldo=0):
        super().__init__(numero, titular, saldo)

    def depositar(self, saldo):
        print("Depositar")
        valor = float(input("Valor a ser depositado: "))
        while valor <= 0:
            print("Impossível depositar valor negativo ou nulo.")
            valor = float(input("Valor a ser depositado: "))
        print("Depósito realizado. Valor adicionado = R$", valor)
        return saldo + valor

    def sacar(self, saldo):
        print("Sacar")
        limite = -5000
        valor = float(input("Valor do saque:"))
        while valor < 0:
            print("Impossível sacar valor negativo.")
            valor = float(input("Valor do saque: "))
        while saldo - valor < limite:
            print("Impossível retirar mais que o limite do cheque-especial. Operação não realizada.")
            valor = float(input("Valor do saque:"))
        print("Saque realizado. Valor retirado = R$" , valor)
        return saldo - valor

    def calcularSaldo(self):
        print("Calcular Saldo")
        print("Saldo atual = R$", saldo)


class ContaPoupanca(ContaCorrente):

    def __init__(self, numero, titular, saldo = 0):
        super().__init__(numero, titular, saldo)

    def depositar(self, saldo):
        print("Depositar")
        valor = float(input("Valor a ser depositado: "))
        while valor <= 0:
            print("Impossível depositar valor negativo ou nulo.")
            valor = float(input("Valor a ser depositado: "))
        print("Depósito realizado. Valor adicionado = R$", valor)
        saldo += valor
        return saldo

    def sacar(self, saldo):
        print("Sacar")
        limite = 0
        valor = float(input("Valor do saque:"))
        while valor < 0:
            print("Impossível sacar valor negativo.")
            valor = float(input("Valor do saque: "))
        while saldo - valor < limite:
            print("Impossível negativar saldo. Saque não realizado.")
            valor = float(input("Valor do saque:"))
        print("Saque realizado. Valor retirado = R$" , valor)
        return saldo - valor

    def calcularSaldo(self):
        print("Calcular Saldo")
        print("Saldo atual com juros = R$", saldo*1.05)


if __name__ == '__main__':
    print("\nBem-vindo(a) ao Banco Sssss\n")
    print("Informe seus dados")
    numero = input("Número da conta: ")
    titular = input("Nome do titular: ")

    opt = 0
    while opt != 1 or opt != 2:
        opt = int(input("Informe o tipo da conta: \n(1) - Corrente\n(2) - Poupança\n"))

        if opt == 1:
            print("Conta corrente escolhida.")

            saldo = float(input("Informe seu saldo: "))
            while saldo < -5000:
                print("Saldo inválido")
                saldo = float(input("Informe seu saldo: "))
            print("Saldo = R$", saldo)

            conta = ContaCorrente(numero, titular, saldo)

            servico = 0
            while servico != 5:
                servico = int(input("Serviços:\n(1) - Depositar\n(2) - Sacar\n(3) - Calcular saldo\n(4) - Consultar dados\n(5) - Sair\n"))
                if servico < 1 or servico > 5:
                    print("Opção inválida.")
                else:
                    if servico == 1:
                        saldo = conta.depositar(saldo)
                    elif servico == 2:
                        if saldo > -5000:
                            saldo = conta.sacar(saldo)
                        else:
                            print("Você está no limite do cheque especial. Não é possivel realizar mais saques.")
                    elif servico == 3:
                        conta.calcularSaldo()
                    elif servico == 4:
                        conta.mostrarDados(numero, titular, saldo)
                    else:
                        print("Sair")
        elif opt == 2:
            print("Poupança escolhida.")

            saldo = float(input("Informe seu saldo: "))
            while saldo < 0:
                print("Saldo inválido")
                saldo = float(input("Informe seu saldo: "))
            print("Saldo = R$", saldo)

            conta = ContaPoupanca(numero, titular, saldo)

            servico = 0
            while servico != 5:
                servico = int(input("Serviços:\n(1) - Depositar\n(2) - Sacar\n(3) - Calcular saldo\n(4) - Consultar dados\n(5) - Sair\n"))
                if servico < 1 or servico > 5:
                    print("Opção inválida.")
                else:
                    if servico == 1:
                        saldo = conta.depositar(saldo)
                    elif servico == 2:
                        if saldo > 0:
                            saldo = conta.sacar(saldo)
                        else:
                            print("Você está sem saldo. Impossível realizar saque.")
                    elif servico == 3:
                        conta.calcularSaldo()
                    elif servico == 4:
                        conta.mostrarDados(numero, titular, saldo)
                    else:
                        print("Sair")
        else:
            print("Opção inválida.")
