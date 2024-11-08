import sys


def main():
    #dont forget to check args
    mileage = int(sys.argv[1])
    theta0 = 0
    theta1 = 0
    estimatePrice = theta0 + (theta1 * mileage)


if __name__ == "__main__":
    main()