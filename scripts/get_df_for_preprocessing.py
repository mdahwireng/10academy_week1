import pandas as pd

class GetDfForPreprocessing:
    """
    this function will prepare data form dataframe for preprocessing
    
    Return
    ------
    dataframe
    """
    def __init__(self, df:pd.DataFrame):
        
        self.df = df
        
    def print_df_info(self) -> None:
        """
        this function will print the info of the datafame

        Return
        ------
        None
        """
        print('Retrieving info from data...')
        #save the number of columns and names
        col_info = 'The number of colum(s): {}.\nThe column(s) is/are : {} and {}\n'.format(len(self.df.columns),', '.join(self.df.columns[:-2]), self.df.columns[-1])  
        
        #save the number of rows
        num_rows = "\nThe total number of rows: {}".format(len(self.df))
        
        na_cols = self.df.columns[self.df.isnull().any()]
        
        #save the number of missing values
        num_na_cols = "\nThe number of columns having missing value(s): {}".format(len(na_cols))
        
        #save the columns with missing value and the num of values missing
        na_cols_num_na = ''
        
        na_col_val_dict = {}
        for col in na_cols:
            missing_vals = self.df[col].isnull().sum()
            na_col_val_dict[col] = missing_vals
            na_cols_num_na += "\nThe number of rows with missing value(s) in [{}]: {}".format(col, missing_vals)
        
        # save the total number of missing values
        tot_na = "\nThe total number of missing value(s): {}".format(self.df.isnull().sum().sum())
        
        self.na_cols = na_cols
        self.na_col_val_dict = na_col_val_dict
        
        print(col_info, num_rows, num_na_cols, na_cols_num_na)
        
        
    def drop_cols_abv_na_trshld(self, threshold:float) -> pd.DataFrame:
        """
        this function will drop columns with missing values above a specified threshold

        Return
        ------
        dataframe
        """
        print('\nComparing threshold with fraction of missing values ...')
        df = self.df
        try:
            if self.na_col_val_dict:
                na_col_val_dict = self.na_col_val_dict
                na_cols = self.na_col_val_dict
        except:
            na_cols = df.columns[df.isnull().any()]
            na_col_val_dict = {}
            for col in na_cols:
                missing_vals = df[col].isnull().sum()
                na_col_val_dict[col] = missing_vals
            
        tot_entries = len(df)
        above_treshold = []
        
        print('\nRetrieving columns to be dropped ...')
        for col in na_cols:
            if na_col_val_dict[col] > threshold * tot_entries:
                above_treshold.append(col)
                
        print('\nColumns to be dropped :', above_treshold)
                
        print('\nDropping columns with missing values above the threshold ...') 
        df.drop(above_treshold, axis=1, inplace=True)
        
        return df  