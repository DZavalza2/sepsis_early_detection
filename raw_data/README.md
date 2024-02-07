# Processed Data

## Brief Introduction
The repository consists of a few Python and SQL scripts which assist in created our cleaned data from the original dataset.

The repository is organized and used in the following:

`extract.sql` - Contains sql queries used to extract valid patients data we can use for our dataset (specifically vital signs). 

`merge.ipynb` - Contains python code walking viewers through merging all patient data gathered from the sql queries above according to the appropriate time and patient information.

`HeartRate_clean.csv` - DataFrame containing patients id and their hourly heart rate. Used to merge into merged.csv with all other hourly vital signs. 

`RR_clean.csv` - DataFrame containing patients id and their hourly respitory rate. Used to merge into merged.csv with all other hourly vital signs. 

`WBC_clean.csv` - DataFrame containing patients id and their white blood cells. Used to merge into merged.csv with all other hourly vital signs. 

`temp_clean.csv` - DataFrame containing patients id and their hourly temperatures. Used to merge into merged.csv with all other hourly vital signs. 

`merged.csv` - Final DataFrame with patients id's and their hourly vital signs.  

