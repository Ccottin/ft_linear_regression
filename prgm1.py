from load_csv import load, save
from display import display_dots
from pandas import DataFrame, options
import sys
from math import sqrt, isclose


def print_tests(data, vars, tmptheta0, tmptheta1):
    options.display.float_format = '{:.2f}'.format
    print(data)
    print("mse = ", vars['prev_rmse'])
    print("theta0 = ", vars['theta0'])
    print("theta1 = ", vars['theta1'])
    print("tmptheta0 = ", tmptheta0)
    print("tmptheta1 = ", tmptheta1)


def estimate_price(mileage: float, theta0: float, theta1: float) -> int:
    return (theta0 + (theta1 * mileage))


# apply linear regression forumla to find theta0 and theta1 :
# tetha0 -= learningrate * 1/size of data * sum(estimatedPrice - price)
# tetha1 -= learningrate * 1/size of data * sum((estimatedPrice - price) * mileage)
# of course, estimated price is calculated for each value, then added
def linear_regression(vars, data: DataFrame):
    data['estimated price'] = None
    data['error'] = None
    data['coeff'] = None

    for i in range(len(data)):
        data.at[i, 'estimated price'] = estimate_price(data.at[i, 's_km'],
                                                       vars['theta0'],
                                                       vars['theta1'])
    data['error'] = data['estimated price'] - data['price']
    data['coeff'] = data['error'] * data['s_km']

    tmptheta0 = (vars['learning_rate']) * (data['error'].sum() * (1 / len(data)))
    tmptheta1 = (vars['learning_rate']) * (data['coeff'].sum() * (1 / len(data)))
    vars['theta0'] -= tmptheta0
    vars['theta1'] -= tmptheta1

    # compare mse ; if prev and new are equals, we reached climax of parabol
    mse = get_mse(data)
    if isclose(mse, vars['prev_mse'], abs_tol=1e-10):
        return 1
    vars['prev_mse'] = mse

    # uncomment this line to see what happend under the hood
    # print_tests(data, vars, tmptheta0, tmptheta1)
    evaluate_model(data, vars)
    display_dots(data, vars)
    return 0


# la standardisation transforme les donnees pour qu elles aient une moyenne de 0 et un ecart type de 1
# ecart-type = dispersion des donnees :  on retire la moyenne des results, on cherche l ecart-type
# (squrt((nouvelles_vals^2)/nbvals)), enfin on divise chaque valeur par l'ecart type
def standardise(data: DataFrame, vars):
    temp = DataFrame(columns=['t_km'])

    mean_km = data['km'].sum() / len(data)
    data['s_km'] = (data['km'] - mean_km)
    temp['t_km'] = data['s_km'] ** 2
    tmp = temp['t_km'].sum()
    std_km = sqrt(tmp / len(data))
    data['s_km'] /= std_km

    vars['std_km'] = std_km
    vars['mean_km'] = mean_km


# mse = carre de la moyenne des erreurs -> plus il est proche de 0, plus
# le modele se rapproche du juste
def get_mse(data) -> float:
    temp = (data['price'] - data['estimated price']) ** 2
    return temp.sum() * ( 1 / len(data))


def get_m_mse(data) -> float:
    mean = data['price'].sum() / len(data)
    temp = (data['price'] - mean) ** 2
    return temp.sum() * (1 / len(data))


# compare les resultats obtenus avec la moyenne des resultats de base
# si < 0, c'est pire que faire la moyenne des valeurs rééelles
# si == 0, c'est comme faire la moyenne
# si == 1, c'est un modèle parfait 
def evaluate_model(data, var):
    precision = 1 - (var['prev_mse'] / var['m_mse'])
    print("\rModel Precision:", round(precision * 100, 7), "%        ", end="")


def main():
    try:

        assert len(sys.argv) == 2, "Please provide a data file"
        data = load(sys.argv[1])
        if data is None:
            return
        # Change this line to see how learning rate can affect the model
        learning_rate = 0.2
        vars = {'theta0': 0, 'theta1': 0, 'learning_rate': learning_rate,
                'prev_mse': 0, 'm_mse': get_m_mse(data)}

        standardise(data, vars)
        while True:
            if linear_regression(vars, data) == 1:
                break

        print("\n")
        # de-standardize thetas, so they can work with regular inputs 
        theta1 = vars['theta1'] / vars['std_km']
        theta0 = vars['theta0'] - (theta1 * vars['mean_km'])
        save("./thetas", theta0, theta1)

    except Exception as e:
        print("Error: ", str(e))


if __name__ == "__main__":
    main()
