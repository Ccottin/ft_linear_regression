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
        data.at[i, 'estimated price'] = estimate_price(data.at[i, 'price'],
                        variables['teta0'], variables['teta1'])
        data.at[i, 'error'] = data.at[i, 'estimated price'] - data.at[i, 'price']
        data.at[i, 'coeff'] = data.at[i, 'error'] * data.at[i, 'km']
    variables['teta0'] -= data['error'].sum() * 1/len(data) * variables['learning_rate']
    variables['teta1'] -= data['coeff'].sum() * 1/len(data) * variables['learning_rate']
    print(data)
    print(variables['teta0'])
    print(variables['teta1'])
    display_dots(data, variables)


def main():
    try:

        assert len(sys.argv) == 5, "Please provide a single file and teta values"
        data = load(sys.argv[1])
        teta0 = float(sys.argv[2])
        teta1 = float(sys.argv[3])
        learning_rate = float(sys.argv[4])
        variables = {'teta0': teta0, 'teta1': teta1, 'learning_rate': learning_rate}
        for i in range(3):
            linear_regression(variables, data)

    except Exception as e:
        print("Error: ", str(e))
        traceback.print_exc()


if __name__ == "__main__":
    main()
