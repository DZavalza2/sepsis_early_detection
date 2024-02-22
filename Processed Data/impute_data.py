def impute_data(data, num_stds=2):
    """
    This function will take in a DataFrmae (merged data) and impute all the missing values with
    num_stds stand deviations out from the mean. In other words if our calculated mean is 10
    and our std is 3, and our num_std is 2, then we will fill in values based on the range of 
    (10 - 3(2), 10+ 3(2)) or (4,16). Note a higher value for num_stds will result in more random
    variety while a lower number of num_stds will result in less variety. This function will only
    impute data for columns temperature, heart rate, and respitory rate. White blood cells are 
    also imputed based on a backfill (if none, then theyre filled in with the mean).

    -------------------
    Parameters:
    1. data: Pandas DataFrame containing all merged data as we saw on merged.csv
    2. num_stds: The number of stds from the mean you want to impute your data
    """
    def get_mean_std(data, col):
        """
        Helper function to return the mean  and standard deviation of a specific data's column. 
        -----------
        Parameters:
        1. data: Pandas DataFrame containing all merged data as we saw on merged.csv
        2. col: the column name you want to get the mean and std of.
        """
        std = data[col].describe().loc['std']
        mn = data[col].describe().loc['mean']
        return mn, std
    
    def fill_na(data, col):
        """
        Helper function used to fill null values based on a range of the mean plus or minus num_stds
        we defined. 
        ----------------
        Parameters: 
        1. data: Pandas DataFrame containing all merged data as we saw on merged.csv
        2. col: the column name you want to get the mean and std of.
        """
        total_null = data[col].isna().sum()
        mn, std = get_mean_std(data, col)
        mean_vary = np.random.choice(np.arange(mn-(std*num_stds), mn + (std*num_stds) + 1), total_null)
        null_indices = data[col].isna()
        data.loc[null_indices, col] = mean_vary
        return data
    cols = ['temp', 'HeartRate', 'RR']
    for col in cols:
        data = fill_na(data, col)
    data.WBC.replace(to_replace=['<0.1*', 'no data', '.', 'ERROR', '<0.1'], value=np.nan, inplace=True)
    data.WBC = data.WBC.apply(float)
    data['WBC'] = data.groupby('subject_id').WBC.fillna(method = 'ffill')
    data['WBC'] = data.WBC.fillna(data.WBC.mean())
    return data