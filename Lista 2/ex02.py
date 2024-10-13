class Motor:
    def status(self):
        return "Ok"


class Pneu:
    def status(self):
        return "Defeituoso"


class Veiculo(Motor, Pneu):
    def status(self):
        motor = Motor()
        pneu = Pneu()
        print(motor.status())
        print(pneu.status())


Veiculo().status()
