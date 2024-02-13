# LSTM Model

## Brief Introduction
The folder consists of a couple of Python scripts to create the LSTM model and evaluate it using different metrics.

The folder is organized and used in the following:

`LSTM_Model.py` - A Python script that will take in the training, test, and validation data and will return an LSTM model for you to evaluate.

`confusion_matrix.py` - A Python script which uses your LSTM Model to create a confusion matrix so you can evaulate the accuracy of your model. 

`cost_matrix.py` - A Python script which uses your LSTM Model to create a cost matrix so you can see what the expected cost of using your model may be.

`AUROC_Curve.py` - A Python script which uses your LSTM Model to generate a AUROC curve fo ryou to see the tradeoff between your corrected classified patients and incorrectly classified patients. 

`lstm_sepsis.ipynb` - A Python notebook which shows the entire process for many of these python script in a notebook friendly environment. 