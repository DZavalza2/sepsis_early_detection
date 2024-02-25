# Sepsis Early Detection

## Overview
Our team aims to build on the bridge between advanced data science methods and the health care industry by changing the way doctors, nurses, and hospitals identify sepsis in a timely and effective manner. Our project uses a Long Short Term Memory (LSTM) model to forecast the probability of a patient developing sepsis up to 6 hours before current methods diagnose patients. By leveraging advanced machine learning algorithms and data science methods, we are able to take multiple features such as vital signs, patient backgrounds, and more to design a predictive model allowing health care professionals to diagnose and treat patients at an earlier stage, resulting in prompt intervention and lowering patients' chances of death.

## Contributors
- Colin Tran: [ctt005@ucsd.edu](mailto:ctt005@ucsd.edu)
- Zhuji (Jerry) Zhang: [zhz044@ucsd.edu](mailto:zhz044@ucsd.edu)
- Diego Zavalza: [dzavalza@ucsd.edu](mailto:dzavalza@ucsd.edu)
- Asif Mahdin: [amahdin@ucsd.edu](mailto:amahdin@ucsd.edu)
- Mentored by Professor Kyle Shannon: [kshannon@ucsd.edu](mailto:kshannon@ucsd.edu)

## Purpose
The capstone project aims to apply advanced data science techniques to critical health care data, specifically focusing on detecting sepsis in patients before any current methods for diagnosing patients. By finding an accurate probability of a patients risk of obtaining sepsis after later, health care professional are able to effectively treat and potentially lower a patients chances of death. Since no model is ever perfect, this software is expected to be used in  conjunction with health care workers experienced knowledge and protocols. 

## Accessing the Data
To access the MIMIC-III database:
1. Complete an approved course from CITI Training Courses: [CITI Training Courses](https://physionet.org/about/citi-course/)
2. Upload your passing certificate to PhysioNet and apply for access to the database.
3. Once approved, you will gain access to all files in the MIMIC-III database.

## Setting Up the Database
Set up the MIMIC-III database in pgAdmin by following the tutorial provided by the MIT Laboratory for Computational Physiology: [Setting up MIMIC-III in a local Postgres database](https://github.com/MIT-LCP/mimic-code/blob/main/mimic-iii/buildmimic/postgres/README.md).

## Data Preparation
After downloading the data files from the MIMIC-III database, you will have to do some data cleaning to get the same subset of data we are using. By following the steps below, you should have the same csv files we are using (conviently stored in the github repo Raw Data/All_Raw_CSVs). 
1. Run the `Extract_Queries.sql` code on your database to extract the proper vital signs datapoints into a single csv for each vital sign.
2. Using the `merge_vital_signs.py` code, pass all you Pandas DataFrames from step 1 into the function to merge all vital signs together to formulate your new merged DataFrame.
Using those two steps, your merged DataFrame should contain hourly patient data for their white blood cells, temperature, respitory rate and heart rate. You may noticed that many of your datapoints are null but, these values will be imputed in following steps. 

## Data Processing
Using the same DataFrame achieved in the Data Preparation, we are now going to process the data so its ready for our model. Please follow the steps below after reading each functions docstring for implmentation guide.
1. Using the `impute_data.py` file, pass in your DataFrame with the merged vital signs and you will get another DataFrame with all nulls filled in. The process is stated in the docstring.
2. Now using your imputed results, we can calculate if a patient would be called code sepsis using UCSD Health Protocol (more info on this protocol in the docstring). Pass in your imputed results to the `create_sepsis_label.py` which returns the same DataFrame with an added binary column determining if the patient would've gotten called code sepis.
    1. For comparison, our results are shown in `imputed_data.csv`
3. Using your imputed data, run `Create_Training_Test_Val_Data.py` to create the training, testing, and validation data. These will be saved as .npy files.
    1. You can compare your data with our data in `Training_Test_Val_Data.zip`.

## Using the LSTM Model
Now that you have processed your data, you are able to run the model and get early predicitons. 
1. Using your training, testing, and validation, run the `LSTM_Model.py` on your data and you should get back the model ready for predictions (This may take some time).
2. Given the model's output, you can run the `ROC_Curve.py` file to find the ROC Curve, thus giving you a tradeoff percentage of the number of true positives and the false negatives. 
3. Given the model's output, you can run the `confusion_matrix.py` file to find the number of True Positives, True Negatives, False Negatives, and False Positives.
4. Given the models confusion matrix, you can determine a cost for detecting a False Positive and False Negative and see what the cost associated with your data and model using the `cost_matrix.py`. 

