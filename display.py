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

    # fonction de cout 1/2m * pourchaque i((theta1 * xi) - yi)²
    plt.subplot(1, 2, 2)
    cost = DataFrame(columns=['x_values', 'y_values'])
    cost['x_values'] = np.linspace(-1200, -100, 1000)
     # Essaie une large plage
    tmp_array = []
    for theta1 in cost['x_values']:
        cost['predicted'] = theta1 * data['s_km']  # Prédictions h_theta(x)
        cost['squared_error'] = (cost['predicted'] - data['price']) ** 2  # Erreur quadratique
        temp = (1 / (2 * len(data))) * cost['squared_error'].sum()  # Fonction de coût J(theta1)
        tmp_array.append(temp) 
    cost['y_values'] = tmp_array
    plt.plot(cost['x_values'], cost['y_values'], label="Courbe de coût")
    plt.grid(True)
    cost['predicted'] = vars['theta1'] * data['s_km']
    cost['squared_error'] = (cost['predicted'] - data['price']) ** 2  # Erreur quadratique
    actual_cost = (1 / (2 * len(data))) * cost['squared_error'].sum()  # Fonction de coût J(theta1)
    
    plt.scatter(vars['theta1'], actual_cost, color='red', label=f"Theta1 ({vars['theta1']:.2f})")
    
    
    plt.draw()
    plt.pause(0.005)
    plt.clf()