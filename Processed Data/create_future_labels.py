#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import GroupShuffleSplit
from sklearn.preprocessing import StandardScaler


# In[5]:


import warnings
warnings.filterwarnings('ignore')


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


# In[18]:


# Assuming the initial split into train_data and test_data is done
gss_val = GroupShuffleSplit(test_size=0.25, n_splits=1, random_state=42)  
# Create validation set from training data
train_inds, val_inds = next(gss_val.split(train_data, groups=train_data['subject_id']))

new_train_data = train_data.iloc[train_inds]
val_data = train_data.iloc[val_inds]

# Initialize the scaler
scaler = StandardScaler()

# Scale features for the entire dataset before splitting into sequences
# This assumes the features are similar across all sets and can be scaled in one go
# Note: This is a simplification and may not always be the best approach. Consider scaling within each subject loop if data distributions vary significantly by subject.
all_data = pd.concat([new_train_data, val_data, test_data])
all_features_scaled = scaler.fit_transform(all_data[['temp', 'WBC', 'HeartRate', 'RR']])
all_data.loc[:, ['temp', 'WBC', 'HeartRate', 'RR']] = all_features_scaled

# Split the scaled data back
new_train_data = all_data.iloc[:len(new_train_data)]
val_data = all_data.iloc[len(new_train_data):len(new_train_data) + len(val_data)]
test_data = all_data.iloc[-len(test_data):]

# Initialize lists to hold sequences and labels
X_train, y_train = [], []
X_val, y_val = [], []
X_test, y_test = [], []

# Create sequences and labels for the new training data
for subject_id in new_train_data['subject_id'].unique():
    subject_data = new_train_data[new_train_data['subject_id'] == subject_id]
    subject_sequences, subject_labels = create_sequences_and_labels(subject_data, sequence_length, num_hours_ahead)
    X_train.extend(subject_sequences)
    y_train.extend(subject_labels)

# Create sequences and labels for validation data
for subject_id in val_data['subject_id'].unique():
    subject_data = val_data[val_data['subject_id'] == subject_id]
    subject_sequences, subject_labels = create_sequences_and_labels(subject_data, sequence_length, num_hours_ahead)
    X_val.extend(subject_sequences)
    y_val.extend(subject_labels)

# Create sequences and labels for test data
for subject_id in test_data['subject_id'].unique():
    subject_data = test_data[test_data['subject_id'] == subject_id]
    subject_sequences, subject_labels = create_sequences_and_labels(subject_data, sequence_length, num_hours_ahead)
    X_test.extend(subject_sequences)
    y_test.extend(subject_labels)

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




