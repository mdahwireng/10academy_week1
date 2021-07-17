import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def compare_date_app_usage(df, usage_lst, nrows, ncols, const_col, figsize, xlabel, ylabel):    
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, sharex=True, sharey=True, figsize=figsize)

    index = 0
    print('Creating plots....')
    for ax in axes.flat: 
        x = df[const_col]
        y = df[usage_lst[index]]
        #colors = np.random.random((20, 3))
        sns.set(rc={'figure.figsize':(5,5)})
        sns.scatterplot(x, y, ax=ax)
        ax.tick_params(axis='x', labelsize=16, rotation=45)
        ax.tick_params(axis='y', labelsize=16)
        ax.set_title(usage_lst[index], fontsize=16)
        #ax.set(xticks=np.linspace(0, 10, 6), yticks=np.linspace(0, 10, 6))
        index += 1

    # first column of axes:
    for ax in axes[:, 0]:
        ax.set_ylabel(ylabel)

    # last row
    for ax in axes[nrows-1, :]:
        ax.set_xlabel(xlabel)
    sns.set_context('paper')
    sns.set_style('darkgrid')    
    plt.subplots_adjust(top = 0.96, bottom=0.05, hspace=0.3, wspace=0.4)
    fig.savefig('./img/date_app_usage.jpg')
    print("Chart saved as 'date_app_usage.png' in img directory")
    #plt.show()


def create_pair_plot(df, vars):
    if len(df) > 100000:
        df = df[:100000]
    sns.set(rc={'figure.figsize':(5,5)})
    sns_plot = sns.pairplot(data=df,vars=vars, diag_kind='kde')
    sns.set_context('paper')
    sns.set_style('darkgrid')    
    plt.subplots_adjust(top = 0.96, bottom=0.05, hspace=0.3, wspace=0.4)
    sns_plot.savefig('./img/pair_plot.png')
    print("Chart saved as 'pair_plot.png' in img directory")
    #plt.show()

def create_boxplot(df, filename, chart_title):
    df = df.copy()
    minmax_scaler = MinMaxScaler()
    scaled_data = pd.DataFrame(minmax_scaler.fit_transform(df), columns=df.columns)
    fig, ax = plt.subplots(figsize=(20,15))
    sns.violinplot(ax=ax, data=scaled_data)
    ax.tick_params(axis='x', labelsize=16, rotation=45)
    ax.tick_params(axis='y', labelsize=16)
    ax.set_title(chart_title, fontsize=16)
    save_path = './img/'+filename
    fig.savefig(save_path)
    print('Chart saved as {} in img directory'.format(filename))