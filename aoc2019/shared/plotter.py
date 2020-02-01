import matplotlib.pyplot as plt


def plot(x, y):
    plt.plot(x, y, 'ro')
    plt.axis([0, 50, -10, 10])
    plt.show()
