import polars as pl
import polars.selectors as cs


class OneHotEncoder:
    def __init__(self, df: pl.DataFrame):
        self.df = df
    
    def encode(self) -> pl.DataFrame:
        return self.df.to_dummies(cs.string())