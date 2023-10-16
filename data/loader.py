import pandas as pd
from palmerpenguins import load_penguins

#class to store standard values
class DataScheme:
    YEAR = "year"
    SPECIES = "species"
    ISLAND = "island"

def load_data(path: str) -> pd.DataFrame:
    # load data; could be csv file or other
    #data = pd.read_csv(path)
    data = load_penguins()

    #data cleaning & processing

    return data # type: ignore

