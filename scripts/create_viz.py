import seaborn as sns
import matplotlib.pyplot as plt

def compare_date_app_usage(df, usage_lst, nrows, ncols, const_col, figsize, xlabel, ylabel):    
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, sharex=True, sharey=True, figsize=figsize)

    usage_lst = ['Social Media DL (Bytes)',
        'Social Media UL (Bytes)',
        'Youtube DL (Bytes)',
        'Youtube UL (Bytes)',
        'Netflix DL (Bytes)',
        'Netflix UL (Bytes)',
        'Google DL (Bytes)',
        'Google UL (Bytes)',
        'Email DL (Bytes)',
        'Email UL (Bytes)',
        'Gaming DL (Bytes)',
        'Gaming UL (Bytes)',
        'Other DL (Bytes)',
        'Other UL (Bytes)']

    index = 0
    print('Creating plots....')
    for ax in axes.flat: 
        x = df[const_col]
        y = df[usage_lst[index]]
        #colors = np.random.random((20, 3))
        sns.scatterplot(x, y, ax=ax)
        ax.tick_params(axis='x', labelsize=12, rotation=75)
        ax.tick_params(axis='y', labelsize=12)
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
    sns.set_style()    
    plt.subplots_adjust(top = 0.96, bottom=0.05, hspace=0.3, wspace=0.4)
    fig.save('date_app_usage.jpg')
    plt.show()