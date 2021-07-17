import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def describe(df:pd.DataFrame, stats=['skew', 'mad', 'median', 'kurt'])->pd.DataFrame:
    df = df.copy()
    d = df.describe()
    return d.append(df.reindex(d.columns, axis=1).agg(stats))

def filter_df(df, filter_col_name, filter_value):
    print('Filtering started...')
    seg = df
    filter_ = seg[filter_col_name] > filter_value
    print('\nFiltering completed')
    return seg[filter_]

def get_top10_per_col(df, top_num):
    df=df.copy()
    print('Retrieving columns info...')
    top_num_dict = {}
    for col in df.columns:
        print('Retrieving the top {} from {}'.format(top_num, col))
        top_num_dict[col] = df[col].sort_values(ascending=False).index[:top_num]
    print('Process completed')
    return top_num_dict

def get_engagement_clusters(df, filename, n_clusters):
    df = df.copy()
    sscaler = StandardScaler()
    print('Standardizing input')
    scaled_input = sscaler.fit_transform(df)
    print('Initializing KMeans Classifier')
    k_classifier = KMeans(n_clusters=n_clusters)
    print('Classifying....')
    #k_classifier.fit(scaled_input)

    customer_class = k_classifier.fit_predict(scaled_input)
    df['customer_class'] = customer_class
    colors = np.array(['darkgrey', 'lightsalmon', 'powderblue'])
    fig,ax = plt.subplots(figsize=(20,15))
    print('Creating plots for classified groups...')
    sns.scatterplot(data=df,x='Dur. (ms)', y='Tot_DL_UL (Bytes)', hue='customer_class', legend='full', ax=ax)
    ax.set_xlabel(xlabel='Duration/(ms)',fontsize=20)
    ax.set_ylabel(ylabel='Total upload+download/(ms)',fontsize=20)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)
    ax.set_title('Customer Classification', fontsize=20)
    #plt.legend(label='Cutomer Clusters')

    save_path = './img/'+ filename
    fig.savefig(save_path)
    print('Plot saved as {} in img directory'.format(filename))
    return df


def get_kmeans_k(df, filename):
    df = df.copy()
    sscaler = StandardScaler()
    print('Standardizing input')
    scaled_input = sscaler.fit_transform(df)
    
    K = range(1, 10)
    distortions = []
    print('Initializing KMeans Classifier')
    for k in K:
        k_classifier = KMeans(n_clusters=k)
        print('Classifying....')
        k_classifier.fit(scaled_input)
        #k_classifier.fit(scaled_input)
        print('Evaluating k={} values....'.format(k))
        distortions.append(k_classifier.inertia_)
        
    print('Evaluation completed.')
    print('Ploting started')    
    plt.figure(figsize=(20,15))
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('k', fontsize=20)
    plt.ylabel('Distortion', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title('The Elbow Method showing the optimal k', fontsize=20)
    save_path = './img/'+filename
    plt.savefig(save_path)
    print('Plotting Completed, file saved in img directory as {}'.format(filename))