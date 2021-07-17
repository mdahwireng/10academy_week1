import matplotlib.pyplot as plt
import pandas as pd
from scipy  import stats
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import math

def remove_outliers(df, threshold = 3, method='mean' )->pd.DataFrame:
    print('Iterating through columns of dataframe...')
    df = df.copy()
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
        while len(outlier_pos[0]) != 0:
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

def create_pca(df, num_components)->pd.DataFrame:
    raw_input =  df.copy()
    sscaler = StandardScaler()
    print('Scaling inputs...')
    scaled_pca_input = sscaler.fit_transform(raw_input)
    print('Initializing PCA...')
    pca = PCA(n_components=num_components)
    input_dict = {'scaled_input':scaled_pca_input, 'raw_input': raw_input }
    print('Creating Principal Components for scaled and raw inputs...')
    pca_dict = {i : {'pca_data':pca.fit_transform(input_dict[i]), 'pca':pca} for i in input_dict}
    print('Scoring Principal Components of scaled and raw inputs...')
    for i in pca_dict:
        pca_dict[i]['score'] = pca_dict[i]['pca'].explained_variance_ratio_.sum()
    print('Selecting the Principal Components with the best score...')
    score = 0
    for i in pca_dict:
        if pca_dict[i]['score'] > score:
            pca_dict[i]['name']= i
            selected_pca = [pca_dict[i]]
    print('\nThe selected Principal components retains {}% of the data with a lesser number of features on {}'
        .format(math.trunc(selected_pca[0]['score']*100), selected_pca[0]['name']))
    print('Creating dataframe for selected Principal Components')
    columns = ['principal component ' + str(i+1) for i in range(num_components)]
    componentDf = pd.DataFrame(data = selected_pca[0]['pca_data'], columns = columns)
    print('\nProcesses completed and dataframe for selected Principal Components returned')
    return componentDf