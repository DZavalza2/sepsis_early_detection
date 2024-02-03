def create_sepsis_label(df, temperature, heart_rate, respiratory, wbc):
    """
    Returns a DataFrame that is the same as the input DataFrame except it contains another column named "sepsis"
    which labels if a patient would have gotten code sepsis called based on their vital signs. This protocol is 
    based on UCSD Health code sepsis protocol.
    -------------------------
    Parameters:
    1. df (pd.DataFrame) - DataFrame to extract patient data from 
    2. temperature (str) - Column name in which the patients temperatures are stored as floats
    3. heart_rate (str) - Column name in which the patients heart rates are stored as floats
    4. respiratory (str) - Column name in which the patients respiratory rates are stored as floats
    5. wbc (str) - Column name in which the patients white blood cells are stored as floats
    """
    def code_sepsis(temperature, heart_rate, respiratory, wbc):
        """
        Helper function that returns label 1 if patient data would alert code sepsis, 0 otherwise based on UCSD 
        Health Protocol for code sepsis. If any two conditions meet, code sepsis is called and is investigated
        further. 
        """
        count = 0 
        if temperature > 38.3 or temperature < 36:
            count+= 1
        if heart_rate > 90:
            count+= 1
        if respiratory > 20:
            count+= 1 
        if wbc > 12 or wbc < 4:
            count+= 1

        if count >= 2:
            return 1
        return 0
        
    result = df.apply(lambda row: code_sepsis(row[temperature], row[heart_rate], row[respiratory], row[wbc]), axis=1)
    df['sepsis'] = result
    return df 