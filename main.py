from load_csv import load
from display import display_dots
from pandas import DataFrame
import traceback
import sys

def estimate_price(mileage: float, teta0: float, teta1: float) -> int:
    return (teta0 + (teta1 * mileage))


def linear_regression(variables, data: DataFrame):
    data['estimated price'] = None
    data['error'] = None
    data['coeff'] = None
    for i in range(len(data)):
        data.at[i, 'estimated price'] = estimate_price(data.at[i, 'km'],
                                                       variables['teta0'],
                                                       variables['teta1'])
        data.at[i, 'error'] = data.at[i, 'estimated price'] - data.at[i, 'price']
        data.at[i, 'coeff'] = data.at[i, 'error'] * data.at[i, 'n_km']
    variables['teta0'] -= (variables['learning_rate']) * data['error'].sum() * 1/len(data)
    variables['teta1'] -= (variables['learning_rate']) * data['coeff'].sum() * 1/len(data)
    print(data)
    print("teta0 = ", variables['teta0'])
    print("teta1 = ", variables['teta1'])
    display_dots(data, variables)

#normalisation will prevent getting too big coeeficients later on :
#coefficient of a droite can only me modified by [0,1] or else it makes no sense#
def normalise(data: DataFrame):
    data['n_km'] = (data['km'] - data['km'].min()) / (data['km'].max() - data['km'].min())


def main():
    try:

        assert len(sys.argv) == 5, "Please provide a single file and teta values"
        data = load(sys.argv[1])
        teta0 = float(sys.argv[2])
        teta1 = float(sys.argv[3])
        learning_rate = float(sys.argv[4])
        variables = {'teta0': teta0, 'teta1': teta1, 'learning_rate': learning_rate}
        normalise(data)
        for i in range(50):
            linear_regression(variables, data)
            print("prediction pour 139800 = ", estimate_price(139800, variables['teta0'], variables['teta1']))

    except Exception as e:
        print("Error: ", str(e))
        traceback.print_exc()


if __name__ == "__main__":
    main()
