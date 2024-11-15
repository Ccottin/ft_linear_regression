from load_csv import load
from display import display_dots
from pandas import DataFrame
from pandas import options
import traceback
import sys
from math import sqrt
from sklearn import metrics

def estimate_price(mileage: float, teta0: float, teta1: float) -> int:
    return (teta0 + (teta1 * mileage))

# apply linear regression forumla to find teta0 and teta1 according to previous one
def linear_regression(vars, data: DataFrame):
    data['estimated price'] = None
   # data['n_estimated price'] = None
    data['error'] = None
    data['coeff'] = None

    for i in range(len(data)):
        data.at[i, 's_estimated price'] = estimate_price(data.at[i, 's_km'],
                                                         vars['teta0'],
                                                         vars['teta1'])
        # data.at[i, 'estimated price'] = estimate_price(data.at[i, 'km'],
        #                                                vars['teta0'],
        #                                                vars['teta1'])
        data.at[i, 'estimated price'] = (data.at[i, 's_estimated price'] * 
                                         vars['std_price']) + vars['mean_price']
    data['error'] = data['s_estimated price'] - data['s_price']
    data['coeff'] = data['error'] * data['s_km']
   # data['erroryo'] = abs(data['error'])
    tmpteta0 = (vars['learning_rate']) * (data['error'].sum() * (1 / len(data)))
   # print("testyo = ", data['erroryo'].sum() / len(data))
    tmpteta1 = (vars['learning_rate']) * (data['coeff'].sum() * (1 / len(data)))
    vars['teta0'] -= tmpteta0
    vars['teta1'] -= tmpteta1
    print(data)
   
    # if mse(data) < 0:
    #     return 
    
    print("mse = ", rmse(data), " == ", metrics.root_mean_squared_error(data['price'], data['estimated price']))
   
    print("teta0 = ", vars['teta0'])
    print("teta1 = ", vars['teta1'])
    print("tmpteta0 = ", tmpteta0)
    print("tmpteta1 = ", tmpteta1)
   # display_dots(data, vars)

#normalisation will prevent getting too big coeeficients later on :
#coefficient of a droite can only me modified by [0,1] or else it makes no sense
def normalise(data: DataFrame):
    data['n_km'] = (data['km'] - data['km'].min()) / (data['km'].max() - data['km'].min())
    data['n_price'] = (data['price'] - data['price'].min()) / (data['price'].max() - data['price'].min())


# la standardisation transforme les donnees pour qu elles aient une moyenne de 0 et un ecart type de 1
# ecart-type = dispersion des donnees :  on retire la moyenne des results, on cherche l ecart-type
# (squrt((nouvelles_vals^2)/nbvals)), enfin on divise chaque valeur par l'ecart type
def standardise(data: DataFrame, vars):
    temp = DataFrame(columns=['t_km', 't_price'])

    mean_km = data['km'].sum() / len(data)
    data['s_km'] = (data['km'] - mean_km)
    temp['t_km'] = data['s_km'] ** 2
    tmp = temp['t_km'].sum()
    std_km = sqrt(tmp / len(data))
    data['s_km'] /= std_km

    mean_price = data['price'].sum() / len(data)
    data['s_price'] = (data['price'] - mean_price)
    temp['t_price'] = data['s_price'] ** 2
    tmp = temp['t_price'].sum()
    std_price = sqrt(tmp / len(data))
    data['s_price'] /= std_price

    vars['std_km'] = std_km
    vars['std_price'] = std_price
    vars['mean_km'] = mean_km
    vars['mean_price'] = mean_price

# mse = carre de ma moyenne des erreurs -> plus il est proche de 0, plus c est proche du juste
# le modele se rapproche du juste
def rmse(data) -> float:
    temp = (data['price'] - data['estimated price']) ** 2
    return temp.sum() / len(data)

def main():
    try:

        options.display.float_format = '{:.5f}'.format
        assert len(sys.argv) == 5, "Please provide a single file and teta values"
        data = load(sys.argv[1])
        teta0 = float(sys.argv[2])
        teta1 = float(sys.argv[3])
        learning_rate = float(sys.argv[4])
        vars = {'teta0': teta0, 'teta1': teta1, 'learning_rate': learning_rate}
        #normalise(data)
        standardise(data, vars)
        for i in range(50):
            linear_regression(vars, data)
            print("prediction pour 139800 = ", estimate_price(139800, vars['teta0'], vars['teta1']))
            print("prediction pour 1110 = ", estimate_price(1110, vars['teta0'], vars['teta1']))

    except Exception as e:
        print("Error: ", str(e))
        traceback.print_exc()


if __name__ == "__main__":
    main()
