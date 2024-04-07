
from typing import Literal
from .plots import Distribution, Correlation
from functools import partial

class Plot:
    def __init__(self, df, target=None):
        self.df = df
        self.target = target

    def get_plots(self, config=None):
        """
        Create different plots for a DataFrame.
        
        @param config: Configuration for the plots.
        e.g. config = {
            "distribution": {
                "method": "hist" | "violin" | "kde" (default: hist),
                "columns": ["column1", "column2"] | None (default: all columns)
            },
            "correlation": {
                "method": "pearson" | "spearman" | "kendall" (default: pearson)
            }
        }
        
        Available plots:
        distribution: What kind of distribution is there? 
            Pass in a `method` parameter to get a specific kind of distribution.
            - hist: Histogram
            - violin: Violin plot
            - kde: Kernel Density Estimate
            
        correlation: What is the correlation between columns?
        
        """
        distribution = self._distribution()
        correlation = self._correlation()
        
        return {
            "distribution": distribution,
            "correlation": correlation
        }
    
    def _distribution(self, method: Literal['hist', 'violin', 'kde'] = 'hist', columns=None):
        if columns is None:
            columns = self.df.columns
        return Distribution(method, columns, self.df)
    
    def _correlation(self, method: Literal['pearson', 'spearman'] = 'pearson'):
        return Correlation(self.df, method)
    
    def __repr__(self):
        return """Use get_plots() on this to return a dictionary with the plots
    
"""
    
    