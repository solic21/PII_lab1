import numpy as np
import matplotlib.pyplot as plt


def fuzzy_min(mf, value):
    """
    Final min slicing of MF
    """
    return np.minimum(mf, value)


def fuzzy_union(*mfs):
    """
    Final aggreagation of MFs
    """
    x = np.array(mfs)
    return np.amax(x, axis=0)


def draw_fuzzy_area(x, mf):
    """
    Draws final MF as area
    """
    fig, ax = plt.subplots()
    ax.set_ylabel(r'$\mu$(x)')
    ax.set_xlabel('x')
    ax.set_ylim([0, 1.2])
    ax.plot(x, mf)
    ax.fill_between(x, mf)
    plt.grid(True)
    plt.show()


def draw_lv(lv):
    """
    Draw the linguistic variable
    """
    fig, ax = plt.subplots()
    ax.set_ylabel(r'$\mu$(x)')
    ax.set_xlabel('x')
    ax.set_ylim([0, 1.2])
    for term in lv['terms']:
        x, mf = lv['U'], lv['terms'][term]
        ax.plot(x, mf, label=term)
        ax.legend()

    plt.grid(True)
    plt.title(lv['name'])
    plt.show()


