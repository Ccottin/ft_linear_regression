import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np


def f(x, a, b):
    return a * x + b


def update_graph(data, vars):

    ax = vars['graph_infos'][1][0]
    ax1 = vars['graph_infos'][1][1]

    # print the regression line
    to_print = DataFrame(columns=['x_values', 'y_values'])
    to_print['x_values'] = data['km']
    to_print['y_values'] = data['estimated price']
    ax.plot(to_print['x_values'],
            to_print['y_values'],
            color='orange',
            label="regression result")

    # print theta1
    cost = DataFrame(columns=['x_values', 'y_values'])
    cost['predicted'] = vars['theta1'] * data['s_km']
    cost['squared_error'] = (cost['predicted'] - data['price']) ** 2
    actual_cost = (1 / (2 * len(data))) * cost['squared_error'].sum()
    theta1 = ax1.scatter(vars['theta1'],
                         actual_cost,
                         color='red',
                         label=f"Theta1 ({vars['theta1']:.2f})")

    ax.legend()
    ax1.legend()
    plt.draw()
    plt.pause(0.005)
    line = ax.lines[-1]
    line.remove()
    theta1.remove()


# fonction de cout 1/2m * somme de : pourchaque i: ((theta1 * xi) - yi)²
def set_cost(data):
    # calculate cost function to print curb later on
    cost = DataFrame(columns=['x_values', 'y_values'])
    cost['x_values'] = np.linspace(-1500, -100, 1000)
    tmp_array = []
    for theta1 in cost['x_values']:
        cost['predicted'] = theta1 * data['s_km']
        # Erreur quadratique
        cost['squared_error'] = (cost['predicted'] - data['price']) ** 2
        temp = (1 / (2 * len(data))) * cost['squared_error'].sum()
        tmp_array.append(temp)
    cost['y_values'] = tmp_array
    return cost


# Figure = fenetre
# Axes = zone ou le dessin est effectue
# plot est une representation de donnee dans un axe
# subplot = axe organise dans une grille
def init_graph(data):
    fig, (ax, ax1) = plt.subplots(1, 2, figsize=(14, 10))

    # print all dots
    ax.plot(data['km'], data['price'], 'o', label='cars')

    ax.set_title('Linear Regression')
    ax.set_ylabel('Price')
    ax.set_xlabel('Kilometers')
    ax.set_ylim(-1000, data['price'].max() + 1000)
    ax.grid(True)

    # print cost curb
    cost = set_cost(data)
    ax1.plot(cost['x_values'],
             cost['y_values'],
             label="Cost curb")
    ax1.set_title('Error Parabol visualisation')
    ax1.grid(True)
    return (fig, (ax, ax1))
