import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame


def f(x, a, b):
    return a * x + b

def display_dots(data, vars):

    plt.subplot(1, 2, 1)
    # print all dots
    plt.plot(data['km'], data['price'], 'o', label='cars')

    # print the line
    to_print = DataFrame(columns=['x_values', 'y_values'])
    to_print['x_values'] = data['km']
    to_print['y_values'] = data['estimated price']
    plt.plot(to_print['x_values'], to_print['y_values'], label="regression result")
    plt.title('Car for sale')
    plt.ylabel('Price')
    plt.xlabel('Kilometers')
    plt.legend()
    plt.ylim(-1000, data['price'].max() + 1000)
    plt.grid(True)

    # fonction de cout 1/2m * pourchaque i(theta1 µ* xi - yi)²
    plt.subplot(1, 2, 2)
    cost = DataFrame(columns=['x_values', 'y_values'])
    cost['x_values'] = data['s_km']
    predicted = data['s_km'] * vars['theta1']
    cost['y_values'] = np.linspace(-1000, data['price'].max() + 1000, 24)
    cost['y_values'] = np.mean((predicted - data['price']) ** 2)
    print(cost)
    plt.plot(cost['x_values'], cost['y_values'], label="cost curb")
    plt.grid(True)
    
    
    plt.draw()
    plt.pause(0.005)
    plt.clf()