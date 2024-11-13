import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame


def f(x, a, b):
    return a * x + b

def mse(data, to_print):
    print(data)
    to_print['error'] = data['estimated price'] * data['estimated price'] * 1 / len(data)

def display_dots(data, variables):

    to_print = DataFrame(columns=['x_values', 'y_values', 'error'])

    to_print['x_values'] = np.linspace(-100, 100, 100)
    to_print['y_values'] = f(to_print['x_values'], variables['teta1'], variables['teta0'])
    mse(data, to_print)
    


    plt.title('Car for sale')
    plt.ylabel('Price')
    plt.xlabel('Kilometers')

    plt.plot(data['km'], data['price'], 'o', label='points')
    plt.plot(to_print['x_values'], to_print['y_values'], label="courbe")
    plt.plot(data['estimated price'], to_print['error'], label="errors")
    plt.legend()

    plt.xlim(-10000, data['km'].max() + 10000)
    plt.ylim(-1000, data['price'].max() + 1000)
    plt.ylim()
    plt.grid(True)
    data.set_index('km')

    plt.show()
    plt.close()
