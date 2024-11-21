import pandas as pd
from pandas import DataFrame


# it takes km, price as a header and generates index for every line. both are out the table
# so values starts at [0,0]
def load(path: str) -> DataFrame:
    """takes a path as argument, writes the dimensions of the data set
    and returns it."""
    try:
        data = pd.read_csv(path)
        return (data)
    except Exception as e:
        print("Error:", str(e))
        return None

def save(path:str, theta0:float, theta1:float) :
    """save thetas into a csv for later uses"""
    df = DataFrame({"theta0": [theta0], "theta1": [theta1]})
    df.to_csv('thetas.csv', index=False)