import pandas as pd

def describe(df:pd.DataFrame, stats=['skew', 'mad', 'median', 'kurt'])->pd.DataFrame:
    d = df.describe()
    return d.append(df.reindex(d.columns, axis=1).agg(stats))

def filter_df(df, filter_col_name, filter_value):
    print('Filtering started...')
    seg = df
    filter_ = seg[filter_col_name] > filter_value
    print('\nFiltering completed')
    return seg[filter_]