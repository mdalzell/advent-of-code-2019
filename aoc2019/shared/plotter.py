import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


def plot(x, y):
    plt.plot(x, y, 'ro')
    plt.axis([0, 50, -10, 10])
    plt.savefig("./registration-id.png")
