from load_csv import load
from display import display_dots
from pandas import DataFrame
import sys

def estimate_price(mileage: int, teta0: int, teta1: int) -> int:
    return (teta0 + (teta1 * mileage))


def linear_regression(teta0: int, teta1: int, data: DataFrame):
    data['estimated price'] = None
    data['error'] = None
    data['coeff'] = None
    for i in range(len(data)):
        data.at[i, 'estimated price'] = estimate_price(data.at[i, 'price'], teta0, teta1)
        data.at[i, 'error'] = data.at[i, 'price'] - data.at[i, 'estimated price']
        data.at[i, 'coeff'] = data.at[i, 'error'] * data.at[i, 'km']
    tmpteta0 = data['error'].sum() * 1/len(data)
    tmpteta1 = data['coeff'].sum() * 1/len(data)
    print(data)
    print(tmpteta0, data['error'].mean())
    print(tmpteta1)
    display_dots(data, tmpteta0,tmpteta1)


def main():
    try:
        assert len(sys.argv) == 4, "Please provide a single file and teta values"
        data = load(sys.argv[1])
        teta0 = float(sys.argv[2])
        teta1 = float(sys.argv[3])
        print(data)
        linear_regression(teta0, teta1, data)

    except Exception as e:
        print("Error: ", str(e))


if __name__ == "__main__":
    main()
