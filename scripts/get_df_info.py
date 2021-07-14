import pandas as pd

def describe(df:pd.DataFrame, stats=['skew', 'mad', 'median', 'kurt'])->pd.DataFrame:
    d = df.describe()
    return d.append(df.reindex(d.columns, axis=1).agg(stats))