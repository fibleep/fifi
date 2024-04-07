import pandas as pd
import polars as pl
import matplotlib.pyplot as plt
from typing import List
import statsmodels.api as sm

class TimeSeries:
    def __init__(self, df: pl.DataFrame | pd.DataFrame, target: List[str] | str):
        self.df = df
        self.target = target

    def show(self):
        df = self.df.to_pandas() if isinstance(self.df, pl.DataFrame) else self.df
        self._line_plot(df[self.target])
        self._rolling_mean(df[self.target])
        self._seasonality(df[self.target])
        plt.show()

    def _line_plot(self, df):
        df.plot(figsize=(10, 10))
        plt.title("Time Series")
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.show()

    def _rolling_mean(self, df, window=30):
        mean_df = df.rolling(window=window).mean()
        mean_df.plot(figsize=(10, 10))
        plt.title(f"Rolling Mean with Window {window}")
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.show()

    def _seasonality(self, df):
        decomposition = sm.tsa.seasonal_decompose(df, model="additive")
        decomposition.plot()
        plt.show()
