import numpy as np
import matplotlib.pyplot as plt


class Bisection:
    # Function for which the Bisection method operates

    def equation(self, x):
        return -x**4 + 6*x**3 - 12*x **2 + 3 *x + 5

    def bis(self, a, b):

        roz = []

        for i in range(0,10):
            # Sprawdzamy warunek miejsca zerowego 
            if (self.equation(a) * self.equation(b) > 0):
                break

            x1 = (a + b) / 2

            if (self.equation(x1) == 0):
                break
            elif (self.equation(x1) * self.equation(a) < 0):
                b = x1;
                roz.append(b)
            else:
                a = x1;
                roz.append(a)
        try:
            return np.round(roz[9],2)
        except IndexError:
            pass

    def przedzial(self, a, b):

        L = np.linspace(a, b, 10)
        lista = []
        for i in L:
            lista.append(self.bis(i,i+1))
        return set(lista)

rozw = Bisection().przedzial(-2, 2)
print (rozw)

x = np.linspace(-5,5, 40)
y = []
for i in x:
    y.append(Bisection().equation(i))

rozw = list(rozw)
zero = np.zeros(len(rozw))

plt.plot(rozw,zero, 'o', ms=10)
plt.plot(x,y)
plt.axis([-5,5,-2,2])
#plt.savefig('Bisekcja')
plt.show()


