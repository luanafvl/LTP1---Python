#Using turtle lib with OOP

import turtle as tl


class Forma:
    def desenhar(self, lado):
        pass


class Circulo(Forma):
    def desenhar(self, lado):
        tl.circle(lado)


class Quadrado(Forma):
    def desenhar(self, lado):
        for i in range(4):
            tl.forward(lado)
            tl.left(90)


print("Círculo")
circulo = Circulo()
circulo.desenhar(100)

tl.clear()

print("Quadrado")
quadrado = Quadrado()
quadrado.desenhar(100)
