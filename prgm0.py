import os
from load_csv import load


def main():
    try:
        if os.path.exists("./thetas.csv"):
            file = load("./thetas.csv")
            if file is None:
                return
            theta0 = file['theta0'][0]
            theta1 = file['theta1'][0]
        else:
            theta0 = 0
            theta1 = 0
        mileage_str = input('Enter mileage: ')
        mileage = float(mileage_str)

        estimatedPrice = theta0 + (theta1 * mileage)

        if estimatedPrice < 0:
            print("Your car might be really tired.")
        print("Estimated price :", estimatedPrice)

    except Exception as e:
        print("Error: ", str(e))


if __name__ == "__main__":
    main()
