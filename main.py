import math
import matplotlib.pyplot as plt
import numpy as np
class equation:
    def __init__(self, a, b, c, d):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = int(d)
    
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
        y0 = 0*x
        yy =np.linspace(-300, 300, 100)
        x0 = 0*yy
        plt.plot(x0,yy, 'k')
        plt.plot(x,y0,'k')
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
    def __init__(self, a, b, c, d):
        super().__init__(a,b,c,d)

    def f_derevation(self):
        x = np.linspace(-10, 10, 100)
        y1 = 2*self.a*x + self.b
        plt.plot(x, y1)
        super().f()
    
    def __del__(self):
        print("Сгорел сарай, сгорела хата")

class Integral(Derivation):
    def __init__(self, a, b, c, d):
        super().__init__(a,b,c,d)

    def f_integral(self):
        x = np.linspace(-10, 10, 100)
        y2 = (self.a * x ** 3)/3 + (self.b * x **2)/2 + self.c*x + self.d
        plt.plot(x,y2)
        super().f()

    def __del__(self):
        print("Сгорел сарай, сгорела хата")


input_data =(input("Введите коэффициенты уравнения "))
data = input_data.split()
a1 = int(data[0])
b1 = int(data[1])
c1 = int(data[2])
d1 = int(data[3])
equation1 = Integral(a1,b1,c1,d1)

equation1.roots()
equation1.f_derevation()
equation1.f_integral()