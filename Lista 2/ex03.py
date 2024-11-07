import turtle

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

screen = turtle.Screen()
t = turtle.Turtle()
x = int(input("Ponto x: "))
y = int(input("Ponto y: "))
p = Ponto(x, y)
t.goto(p.x, p.y)
screen.mainloop()
