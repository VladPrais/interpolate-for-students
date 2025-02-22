import numpy as np
import matplotlib.pyplot as plt
import random

def LagrangePolynomial(X, Y, x0):
    N = len(X)
    S = 0
    for i in range(N):
        mul = 1
        for j in range(N):
            if i != j:
                mul *= (x0 - X[j]) / (X[i] - X[j])
        S += Y[i] * mul
    return S

# function for interpolation
def f(x):
    return np.exp(-x) * np.sin(x)

if __name__ == "__main__":
    
    # boundaries
    a = 0
    b = 2 * np.pi

    # step for split points
    h = 0.1
    
    for i in range(2, 8):
        # create the random nodes
        x0 = np.array([random.uniform(a, b) for _ in range(i)])
        # function values in nodes
        y0 = f(x0)
    
        x = np.arange(a, b + h, h)

        plt.scatter(x0, y0, label = "nodes")
        plt.plot(x, LagrangePolynomial(x0, y0, x), label = "polynomial")
        plt.plot(x, f(x), label = "func")

        plt.legend()
        plt.title(f"Interpolation with {i} nodes")
        plt.show()
