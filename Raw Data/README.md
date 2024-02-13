# Raw Data

## Brief Introduction
The folder consists of a few Python and SQL scripts which assist in created our cleaned data from the original dataset.

The folder is organized and used in the following:

`CSV Files` - Folder containing all original csv files obtained by running our sql code from extract.sql. More information on each csv file inside.

`extract.sql` - Contains sql queries used to extract valid patients data we can use for our dataset (specifically vital signs). 

`merge_vital_signs.py` - A python script which takes in all vital sign's csv files in CSV Files folder and merges them into a single cleaned up DataFrame based on patients and their hourly recorded time stamps.

`merge.ipynb` - Contains python code walking viewers through merging all patient data gathered from the sql queries above according to the appropriate time and patient information.
