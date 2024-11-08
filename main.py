from load_csv import load
from display import display_dots
import sys


def linear_regression(data: DataFrame):
    

def main():
    try:
        assert len(sys.argv) == 2, "Please provide a single file."
        data = load(sys.argv[1])
        display_dots(data)
        linear_regression(data)

    except Exception as e:
        print("Error: ", str(e))


if __name__ == "__main__":
    main()
