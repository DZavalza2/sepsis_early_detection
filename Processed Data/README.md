# Processed Data

## Brief Introduction
The repository consists of a couple of Python scripts which assist in creating our cleaned data to process through the LSTM model.

The repository is organized and used in the following:

**create_sepsis_label.py** - A Python script which takes in a processed data and output if a patient would be called for code sepsis based on UC San Diego Health protocol

**create_train_test_split.ipynb** - A Python notebook which shows how to do the train test split on the data so you can train the model on different patients based on their individual time in the ICU unit. 