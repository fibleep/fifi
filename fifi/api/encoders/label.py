import polars as pl
import polars.selectors as cs
from sklearn.preprocessing import LabelEncoder as LE


class LabelEncoder:
    def __init__(self, df: pl.DataFrame):
        self.df = df
    
    def encode(self) -> pl.DataFrame:
        label_encoder = LE()
        for col in self.df.select(cs.string()).columns:
            self.df.replace(col, pl.Series(label_encoder.fit_transform(self.df[col])))
        
        return self.df
        
    
    