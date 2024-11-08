import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """takes a path as argument, writes the dimensions of the data set
    and returns it."""
    try:
        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape)
        return (data)
    except Exception as e:
        print("Error:", str(e))
        return None