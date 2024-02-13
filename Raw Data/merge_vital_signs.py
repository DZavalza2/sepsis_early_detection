def merge_vital_signs(temp_df, wbc_df, hr_df, rr_df):
    """
    After reading in the data revieved from the sql queries in 'extract.sql', read in all DataFrame's and pass them
    throught this function. It will merge them all into a single DataFrame where you will have each patient's hourly
    vital signs.
    ----------------------
    Parameters:
    1. temp_df: DataFrame of patients hourly temperatures as recieved from the SQL queries. 
    2. wbc_df: DataFrame of patients white blood cells as recieved from the SQL queries. 
    3. hr_df: DataFrame of patients hourly heart rates as recieved from the SQL queries. 
    4. rr_df: DataFrame of patients hourly respiratory rate as recieved from the SQL queries. 
    
    """
    temp_df = temp_df.drop(columns = ['hadm_id', 'itemid', 'icustay_id'])
    wbc_df = wbc_df.drop(columns = ['hadm_id', 'itemid', 'icustay_id'])
    hr_df = hr_df.drop(columns = ['hadm_id', 'itemid', 'icustay_id'])
    rr_df = rr_df.drop(columns = ['hadm_id', 'itemid', 'icustay_id'])

    result = temp_df.merge(wbc_df, on=['subject_id', 'hourly_bin'], how='outer', suffixes=('_df1', '_df2'))
    result = result.merge(hr_df, on=['subject_id', 'hourly_bin'], how='outer', suffixes=('', '_df3'))
    result = result.merge(rr_df, on=['subject_id', 'hourly_bin'], how='outer', suffixes=('', '_df4'))

    result = result.drop(columns = ['row_id'])[['subject_id', 'hourly_bin', 'temp', 'WBC', 'HeartRate', 'RR']]

    result = result.sort_values(by=['subject_id', 'hourly_bin']).reset_index().drop(columns = ['index'])

    return result
    








