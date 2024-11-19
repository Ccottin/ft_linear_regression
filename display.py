import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame


def f(x, a, b):
    return a * x + b

def display_dots(data, vars):

    to_print = DataFrame(columns=['x_values', 'y_values', 'error'])

    to_print['x_values'] = data['km']
    to_print['y_values'] = data['estimated price']
    
    plt.title('Car for sale')
    plt.ylabel('Price')
    plt.xlabel('Kilometers')

    plt.plot(data['km'], data['price'], 'o', label='points')
    plt.plot(to_print['x_values'], to_print['y_values'], label="courbe")
    plt.legend()

    # plt.xlim(-10000, data['km'].max() + 10000)
    # plt.ylim(-1000, data['price'].max() + 1000)
    # plt.ylim()
    plt.grid(True)
    data.set_index('km')

    #print("to print = \n", to_print['error'][0:24])
   # print("to print = \n", to_print)

    # plt.show()
    plt.draw()
    plt.pause(0.005)
    plt.clf()