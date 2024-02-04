# Sepsis Early Detection

## Overview
Our team aims to build on the bridge between advanced data science methods and the health care industry by revolutionizing the way doctors, nurses, and hospitals identify sepsis in a timely and effective manner. Our project uses a Long Short Term Memory (LSTM) model to forecast the probability of a patient developing sepsis up to 6 hours before current methods diagnose patients. By leveraging advanced machine learning algorithms and data science methods, we are able to take multiple features such as vital signs, patient backgrounds, and more to design a predictive model allowing health care professionals to diagnose and treat patients at an earlier stage, resulting in prompt intervention and lowering patients' chances of death.

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
### Loading Data into the Local Database
After downloading the data files from the MIMIC-III database, place them in the `raw_data` folder in this repository. The `raw_data` folder is structured to organize the data as downloaded from MIMIC-III. This helps in maintaining consistency and ease of access for further processing. Ensure that the file structure within `raw_data` matches what the processing scripts expect. For instance, if the scripts expect certain CSV files, place those files directly in the `raw_data` folder. If there are specific naming conventions or directory structures that need to be followed for the raw data files, specify them here.

## Data Processing
The `processed_data` folder contains scripts for preprocessing the raw data from MIMIC-III. Run the scripts in the following order to prepare your data for analysis:

- To implement still
