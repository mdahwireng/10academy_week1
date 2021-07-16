import matplotlib.pyplot as plt
import pandas as pd
from scipy  import stats
import numpy as np

def remove_outliers(df, threshold = 3, method='mean' )->pd.DataFrame:
    print('Iterating through columns of dataframe...')
    for col in df.columns:
        colmn = df[col]
        if method == 'median':
            replacer = colmn.median()
        else:
            replacer = colmn.mean()
        # compute the z-score for all values
        print('Computing z-score for values...')
        arr = colmn.values
        z = np.abs(stats.zscore(arr))
        outlier_pos = np.where(z > threshold)
        while len(outlier_pos) != 0:
            print('Replacing outliers in {}'.format(col))
            arr[outlier_pos] = replacer
            # recompute the values to check if the data meets the requirements
            z = np.abs(stats.zscore(arr))
            outlier_pos = np.where(z > threshold)
        df[col] = arr
    print('Outlier removals complete')
    return df

def create_data_partition(df, data_col_name, part_col_name, num_parts)->pd.DataFrame:
    seg = df.copy()
    print('Creating {} partions using data from {}...',format(num_parts,data_col_name))
    seg[part_col_name] = pd.qcut(seg[data_col_name], num_parts,labels = False)
    print('\nDone! Partions saved with column name {}',format(part_col_name))
    return seg

def group_and_sum(df, groupby_col_name, sumby_col_lst)->pd.DataFrame:
    print('Grouping and aggregation in process...')
    seg = df.copy()
    outp = seg.groupby(groupby_col_name)[sumby_col_lst].sum()
    print('\nGrouping and aggregation completed.')
    return outp