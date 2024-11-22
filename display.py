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
    cost['x_values'] = np.linspace(-1200, -100, 1000)
    theta1_range = np.linspace(-1200, -1000, 100) 
     # Essaie une large plage
    cost_values = [] 
    for theta1 in theta1_range:
        cost['prediction'] = theta1 * data['s_km']  # Prédictions h_theta(x)
        cost['squared_error'] = (cost['prediction'] - data['price']) ** 2  # Erreur quadratique
        costt = (1 / (2 * len(data))) * cost['squared_error'].sum()  # Fonction de coût J(theta1)
        cost_values.append(costt)

   # plt.plot(vars['theta1'], vars['theta1'], 'o', label='theta 1')
    print(cost, vars['theta1'])
    plt.plot(theta1_range, cost_values, label="Courbe de coût")
    plt.grid(True)
    cost['prediction'] = vars['theta1'] * data['s_km']
    cost['squared_error'] = (cost['prediction'] - data['price']) ** 2  # Erreur quadratique
    actual_cost = (1 / (2 * len(data))) * cost['squared_error'].sum()  # Fonction de coût J(theta1)
    plt.scatter(vars['theta1'], actual_cost, color='red', label=f"Theta1 ({vars['theta1']:.2f})")
    
    
    plt.draw()
    plt.pause(0.005)
    plt.clf()