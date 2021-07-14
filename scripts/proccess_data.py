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
        z = np.abs(stats.zscore(colmn))
        arr = df[col].values
        outlier_pos = np.where(z > threshold)
        print('Replacing outliers in {}'.format(col))
        arr[outlier_pos] = replacer
        df[col] = arr
    print('Outlier removals complete')
    return df