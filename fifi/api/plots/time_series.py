import pandas as pd
import polars as pl

class TimeSeries:
    def __init__(self, df: pl.DataFrame | pd.DataFrame, target: str):
        self.df = df
        self.target = target