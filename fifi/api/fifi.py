import polars as pl

from .report import Report
from .plot import Plot



class Fifi:
    """
    Main class for accessing the library
    """
    def __init__(self, df: pl.DataFrame, target: str = None):
        """Initialize a new instance of the Fifi class.
        @param df: DataFrame to work with.
        @param target: Target column for supervised learning.
        """
        self.df = df
        self.target = target
    
    def report(self) -> dict:
        """Generate a report for a DataFrame.
        @param df: DataFrame to generate a report for.
        @return: Dictionary containing the report, iterate over it or use each key as needed.
        """
        return Report(self.df)
    
    def plots(self):
        """Create a Plot instance for a DataFrame.
        You can use this to plot different kinds of plots.
        @param df: DataFrame to plot.
        """
        return Plot(self.df)

    def __repr__(self):
        methods = [method for method in dir(self) if callable(getattr(self, method)) and not method.startswith("__")]
        methods_str = ""
        for method in methods:
            doc = getattr(self, method).__doc__
            methods_str += f"{method}: {doc}\n    "
        return f"Welcome to Fifi!\nPossible methods:\n    {methods_str}"