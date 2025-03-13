import math
import matplotlib.pyplot as plt
import numpy as np
class equation:
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
    
    def roots(self):
        discr = self.b ** 2 - 4 * self.a * self.c
        print("Дискриминант D =" , discr)

        if discr > 0:
            x1 = (-self.b + math.sqrt(discr)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discr)) / (2 * self.a)
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        elif discr == 0:
            x = -self.b / (2 * self.a)
            print("x =", x)
        else:
            print("Корней нет")
    def f(self):
        x = np.linspace(-10, 10, 100)
        y = self.a*x**2 + self.b*x + self.c
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('График функции')
        plt.grid(True)
        plt.show()
        return y

    def __del__(self):
        print("Сгорел сарай, сгорела хата")

class Derivation(equation):
    def __init__(self, a, b, c):
        super().__init__(a,b,c)

    def f_derevation(self):
        x = np.linspace(-10, 10, 100)
        y1 = self.a*x*2 + self.b
        y2 = self.a*x**2 + self.b*x + self.c
        plt.plot(x, y1)
        plt.plot(x, y2)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Графики функций и её производной')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def __del__(self):
        print("Сгорел сарай, сгорела хата")

qq = Derivation(1,1,-6)
qq.roots()
qq.f()
qq.f_derevation()
