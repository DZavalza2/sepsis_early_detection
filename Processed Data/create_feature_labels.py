#!/usr/bin/env python
# coding: utf-8

# In[4]:

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GroupShuffleSplit
from sklearn.preprocessing import StandardScaler


# In[6]:


df = pd.read_csv('../imputed_data.csv')
df = df.drop(columns = ['Unnamed: 0'])
df.head()


# In[ ]:


sequence_length = 10
num_hours_ahead = 5


# In[10]:


df['hourly_bin'] = pd.to_datetime(df['hourly_bin'])


# # Labeling the data

# In[11]:


def create_sequences_and_labels(data, sequence_length, num_hours_ahead):
    sequences = []
    labels = []
    for i in range(len(data) - sequence_length - num_hours_ahead + 1):
        sequence = data.iloc[i:i + sequence_length]
        sequences.append(sequence[['temp', 'WBC', 'HeartRate', 'RR']].values)
        
        # Find the hourly_bin at the end of the current sequence
        end_time = pd.to_datetime(sequence.iloc[-1]['hourly_bin'])

        
        # Look ahead in time by num_hours_ahead to check for sepsis
        future = data[(data['hourly_bin'] > end_time) & 
                      (data['hourly_bin'] <= end_time + pd.Timedelta(hours=num_hours_ahead))]
        label = 1 if future['sepsis'].any() else 0
        labels.append(label)
        
    return np.array(sequences), np.array(labels)


# Split subjects into training, validation, and test groups first
unique_subjects = df['subject_id'].unique()
train_subjects, temp_subjects = train_test_split(unique_subjects, test_size=0.4, random_state=42)
val_subjects, test_subjects = train_test_split(temp_subjects, test_size=0.5, random_state=42)

# Split DataFrame based on subjects
train_data = df[df['subject_id'].isin(train_subjects)]
val_data = df[df['subject_id'].isin(val_subjects)]
test_data = df[df['subject_id'].isin(test_subjects)]

# Initialize the scaler and scale features for each dataset
scaler = StandardScaler()
train_features = train_data[['temp', 'WBC', 'HeartRate', 'RR']]
scaler.fit(train_features)  # Fit on training data only

# Apply scaling
train_data.loc[:, ['temp', 'WBC', 'HeartRate', 'RR']] = scaler.transform(train_features)
val_data.loc[:, ['temp', 'WBC', 'HeartRate', 'RR']] = scaler.transform(val_data[['temp', 'WBC', 'HeartRate', 'RR']])
test_data.loc[:, ['temp', 'WBC', 'HeartRate', 'RR']] = scaler.transform(test_data[['temp', 'WBC', 'HeartRate', 'RR']])

# Initialize lists for sequences and labels
X_train, y_train = [], []
X_val, y_val = [], []
X_test, y_test = [], []

# Create sequences and labels for the training data
for subject_id in train_data['subject_id'].unique():
    subject_data = train_data[train_data['subject_id'] == subject_id]
    subject_sequences, subject_labels = create_sequences_and_labels(subject_data, sequence_length, num_hours_ahead)
    X_train.extend(subject_sequences)
    y_train.extend(subject_labels)

# Repeat for validation and test data
for subject_id in val_data['subject_id'].unique():
    subject_data = val_data[val_data['subject_id'] == subject_id]
    subject_sequences, subject_labels = create_sequences_and_labels(subject_data, sequence_length, num_hours_ahead)
    X_val.extend(subject_sequences)
    y_val.extend(subject_labels)

for subject_id in test_data['subject_id'].unique():
    subject_data = test_data[test_data['subject_id'] == subject_id]
    subject_sequences, subject_labels = create_sequences_and_labels(subject_data, sequence_length, num_hours_ahead)
    X_test.extend(subject_sequences)
    y_test.extend(subject_labels)

# Optionally, convert lists to arrays
X_train, y_train = np.array(X_train), np.array(y_train)
X_val, y_val = np.array(X_val), np.array(y_val)
X_test, y_test = np.array(X_test), np.array(y_test)

# Convert lists to numpy arrays
X_train = np.array(X_train)
y_train = np.array(y_train)
X_val = np.array(X_val)
y_val = np.array(y_val)
X_test = np.array(X_test)
y_test = np.array(y_test)

# Convert lists to numpy arrays
X_train = np.array(X_train)
y_train = np.array(y_train)
X_val = np.array(X_val)
y_val = np.array(y_val)
X_test = np.array(X_test)
y_test = np.array(y_test)


# In[25]:


# Save the numpy arrays as .npz files
np.save('data/X_train.npy', X_train)
np.save('data/y_train.npy', y_train)
np.save('data/X_val.npy', X_val)
np.save('data/y_val.npy', y_val)
np.save('data/X_test.npy', X_test)
np.save('data/y_test.npy', y_test)


# In[ ]:




