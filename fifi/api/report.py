import polars as pl

from fifi.utility import bcolors


class Report:
    def __init__(self, df: pl.DataFrame):
        self.df = df

    def info(self, verbose=True) -> dict:
        df = self.df
        shape = df.shape
        columns = df.columns
        dtypes = df.dtypes
        null_count = df.null_count()
        n_unique = df.n_unique()
        print(df.describe())
        # parsed_columns = ""
        # if verbose:
        #     parsed_columns = ""
        #     for col in df.columns:
        #         parsed_columns += f"{bcolors.OKCYAN}\n------ COLUMN: {col} ------"
        #         parsed_columns += f"{bcolors.OKGREEN}\nType: {df[col].dtype}"
        #         parsed_columns += f"{bcolors.OKCYAN}\nRows: {df[col].count()}"
        #         parsed_columns += f"{bcolors.WARNING}\nUnique: {df[col].unique().count()}"
        #         parsed_columns += f"{bcolors.OKBLUE}\nMissing #: {df[col].is_null().sum()}"
        #         parsed_columns += f"{bcolors.HEADER}\nMissing %: {df[col].is_null().mean() * 100:.2f}%\n{bcolors.ENDC}"

        #     print(f"{bcolors.HEADER}## DataFrame Info, thanks for using fifi! ##{bcolors.ENDC}")
        #     print(f"{bcolors.HEADER}--------------------------------------------{bcolors.ENDC}\n")
        #     print(f"{bcolors.BASIC}Shape:{bcolors.INFO}\nX (Rows): {df.shape[0]},\nY (Columns): {df.shape[1]}\n{bcolors.ENDC}")
        #     print(f"{bcolors.BASIC}Columns:{parsed_columns}{bcolors.ENDC}")
        
        return {
            "shape": shape,
            "columns": columns,
            "dtypes": dtypes,
            "null_count": null_count,
            "n_unique": n_unique
        }
    
    def __repr__(self):
        self.info()
        return "Use info() to return a dictionary with the report."