import numpy as np
import matplotlib.pyplot as plt


def equation(x):
    return 6*x**3 - 12*x ** 2 - 3 * x + 5


def bisection(a, b, n=100):
    roots = []
    for j in range(0, n):
        # If the function is not continuous break
        if equation(a) * equation(b) > 0:
            break
        # Divide interval at half
        x1 = (a + b) / 2
        # If the root are find break
        if equation(x1) == 0:
            break
        # Define new smaller interval [a, x1] and [x1, b] according with algorithm
        elif equation(x1) * equation(a) < 0:
            b = x1
            roots.append(b)
        else:
            a = x1
            roots.append(a)
    # If the roots exist return it (the last element of the root list have the best precision
    try:
        return np.round(roots[len(roots)-1], 4)

    except IndexError:
        pass


def interval(a, b):

    interval_steps = np.linspace(a, b, 10)
    results_of_scanning = []

    for k in interval_steps:
        results_of_scanning.append(bisection(k, k + 1))
        # return roots
    return set(results_of_scanning)


# Find root withing the interval a and b
a_initial = -5
b_initial = 5
root = interval(a_initial, b_initial)
print(root)

# For plot function
X = np.linspace(a_initial, b_initial, 40)
y = []
for i in X:
    y.append(equation(i))

root = list(root)
y_zero = np.zeros(len(root))

plt.plot(root, y_zero, 'o', ms=10)
plt.plot(X, y)
plt.axis([a_initial, b_initial, min(y), max(y)+2])
plt.savefig('bisection.png')
plt.show()


