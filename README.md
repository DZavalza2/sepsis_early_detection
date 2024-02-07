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
After downloading the data files from the MIMIC-III database, you will have to do some data cleaning to get the same subset of data we are using. Your best resouce for this is going to be looking at the `extract.sql` file and `merge.ipynb`. In the `extract.sql` file, we provide the queries we used to extract the vital signs from the entire database. Similarly, `merge.ipynb` provides a comprehensive python notebook which guides readers through cleaning up the messy data from the database extraction. Using these two guiding files, users should be able to recreate our subset of data we are using for our model.

## Data Processing
**To implement still**

## 