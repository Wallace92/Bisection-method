import numpy as np
import matplotlib.pyplot as plt

class Bisection:
    # Funkcja dla ktorej liczymy miejsca zerowe
    def funkcja(self, x):
        return 2*x**3 + 3*x **2 + 3 *x + 2

    def bis(self, a, b):


        roz = []

        for i in range(0,10):
            # Sprawdzamy warunek miejsca zerowego
            if (self.funkcja(a) * self.funkcja(b) > 0):
                break

            x1 = (a + b) / 2

            if (self.funkcja(x1) == 0):
                break
            elif (self.funkcja(x1) * self.funkcja(a) < 0):
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
    y.append(Bisection().funkcja(i))

rozw = list(rozw)
zero = np.zeros(len(rozw))

plt.plot(rozw,zero, 'o', ms=10)
plt.plot(x,y)
plt.axis([-5,5,-2,2])
#plt.savefig('Bisekcja')
plt.show()


