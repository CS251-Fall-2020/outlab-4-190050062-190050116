import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.misc import derivative


def fn_plot1d(fn, x_min, x_max, filename):
    vec_fn = np.vectorize(fn)
    X = np.linspace(x_min, x_max)
    Y = vec_fn(X)
    # print(X)
    # print(Y)
    plt.plot(X, Y)
    plt.xlabel("Values of x")
    plt.ylabel("Values of fn(x)")
    plt.title("Plot for fn_plot1d")
    plt.savefig(str(filename))
    plt.clf()


def b(x):
    if x > 0:
        return h(2 - x) / (h(2 - x) + h(x - 1))
    else:
        return h(2 + x) / (h(2 + x) + h(-x - 1))


def h(x):
    if x > 0:
        return np.exp(-1 / (x**2))
    else:
        return 0


def fn_plot2d(fn, x_min, x_max, y_min, y_max, filename):
    vec_fn = np.vectorize(fn)
    x = np.linspace(x_min, x_max)
    y = np.linspace(y_min, y_max)
    X, Y = np.meshgrid(x, y)
    Z = vec_fn(X, Y)
    # print(X)
    # print(Y)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.set_xlabel("Value of x")
    ax.set_ylabel("Value of y")
    ax.set_zlabel("Value of fn(x,y)")
    ax.set_title("Plot for fn2plot")
    plt.savefig(str(filename))
    plt.clf()


def sinc(x, y):
    if np.sqrt(x**2 + y**2) == 0:
        return 0
    else:
        root = np.sqrt(x**2 + y**2)
        return np.sin(root) / root


def nth_derivative_plotter(fn, n, xmin, xmax, filename):
    def deriv(x): return derivative(fn, x, dx=1e-6, n=n)
    vec_fn = np.vectorize(deriv)
    X = np.linspace(xmin, xmax)
    Y = vec_fn(X)
    # print(X)
    # print(Y)
    plt.plot(X, Y)
    plt.xlabel("Values of x")
    plt.ylabel("Values of {} th derivative of fn(x)".format(n))
    plt.title("Plot for {} th derivative of fn(x)".format(n))
    plt.savefig(str(filename))
    plt.clf()


fn_plot1d(b, -2, 2, "fn1plot.png")
fn_plot2d(sinc, -1.5 * np.pi, 1.5 * np.pi, -
          1.5 * np.pi, 1.5 * np.pi, "fn2plot.png")
for i in range(1, 3):
    nth_derivative_plotter(b, i, -2, 2, "bd_{}.png".format(i))
