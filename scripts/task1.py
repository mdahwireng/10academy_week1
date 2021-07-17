#!/usr/bin/env python
# coding: utf-8

# In[9]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from modules.get_df_for_preprocessing import GetDfForPreprocessing, create_agg
from modules.proccess_data import remove_outliers, create_pca
from modules.get_df_info import describe
from modules.create_viz import compare_date_app_usage, create_boxplot, create_pair_plot


# ## Read data

# In[10]:


dfs = pd.read_csv('../data/Week1_challenge_data_source.csv', parse_dates=['Start','End'])


# In[11]:


prep = GetDfForPreprocessing(dfs)
telco_raw = prep.drop_cols_abv_na_trshld(0.3)


# ## slice dataframe for aggreagation

# In[12]:


slice_cols = ['MSISDN/Number',
    'Dur. (ms)',
    'num_xDR_sess',
    'Social Media DL (Bytes)',
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
    'Other UL (Bytes)',
    'Total DL (Bytes)',
    'Total UL (Bytes)']


# In[13]:


telco_agg = create_agg(df=telco_raw, slice_cols=slice_cols, agg_col='MSISDN/Number')


# ## Save aggregated data for fututre use

# In[14]:


telco_agg.reset_index().to_csv('../data/telco_agg.csv')


# ## Removing outliers

# In[15]:


telco_df_processed = remove_outliers(telco_agg)


# In[16]:


telco_df_processed.reset_index().to_csv('../data/telco_df_processed.csv')


# ## Get the statistical description of processed and raw data

# In[17]:


task1_raw_data_desc = describe(df=telco_agg)
task1_proces_data_desc = describe(df=telco_df_processed)



# ## Save the descriptions for presentation

# In[21]:


task1_raw_data_desc.to_csv('../data/task1_raw_data_desc_raw.csv')
task1_proces_data_desc.to_csv('./data/task1_proces_data_desc.csv')


# ## Compare date and data usuage

# In[13]:


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


# In[22]:


compare_date_app_usage(df=telco_raw,  usage_lst=usage_lst, nrows=7, ncols=2, const_col='Start', 
                       figsize=(20,15), xlabel='Date', ylabel='Data (Bytes)')


# ## Create Plots to visualize outliers in raw and processed data

# In[15]:


create_boxplot(df=telco_df_processed, filename='processed_data.png', chart_title='Processed Data')
create_boxplot(df=telco_agg, filename='Unprocessed Data', chart_title='Raw Data')


# ## Creating Principal Components

# In[16]:


pca_df = create_pca(df=telco_df_processed, num_components=2)


# In[17]:




# In[18]:


pca_df.to_csv('../data/pca_df.csv')


# ## Creating Pairplots for features

# In[19]:


vars = ['Tot_DL_UL (Bytes)','Social Media total data (Bytes)','Youtube total data (Bytes)',
        'Netflix total data (Bytes)','Google total data (Bytes)','Email total data (Bytes)','Gaming total data (Bytes)','Other total data (Bytes)']


# In[21]:


create_pair_plot(df=telco_agg , vars=vars)

