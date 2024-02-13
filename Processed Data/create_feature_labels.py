def create_feature_labels(data, sequence_length, num_hours_ahead):
    """

    ---------------------------
    1. data - your clean data as a pandas DataFrame
    2. sequence_length: number of hourly datapoints needed to make predictions (int)
    3. num_hours_ahead: predict if sepsis will be present (num_hours_ahead) hours ahead (int)
    
    """
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
    gss = GroupShuffleSplit(test_size=0.2, n_splits=1, random_state=42)
    train_inds, test_inds = next(gss.split(df, groups=df['subject_id']))

    train_data = df.iloc[train_inds]
    test_data = df.iloc[test_inds]

    # Further split the training data into training and validation sets
    gss_val = GroupShuffleSplit(test_size=0.25, n_splits=1, random_state=42)  
    # Create validation set from training data
    train_inds, val_inds = next(gss_val.split(train_data, groups=train_data['subject_id']))

    new_train_data = train_data.iloc[train_inds]
    val_data = train_data.iloc[val_inds]

    # Initialize the scalerx
    scaler = StandardScaler()

    # Scale features for the new training data
    new_train_features = scaler.fit_transform(new_train_data[['temp', 'WBC', 'HeartRate', 'RR']])
    new_train_data.loc[:, ['temp', 'WBC', 'HeartRate', 'RR']] = new_train_features

    # Scale features for the validation data
    val_features = scaler.transform(val_data[['temp', 'WBC', 'HeartRate', 'RR']])
    val_data.loc[:, ['temp', 'WBC', 'HeartRate', 'RR']] = val_features

    # Scale features for the test data
    test_features = scaler.transform(test_data[['temp', 'WBC', 'HeartRate', 'RR']])
    test_data.loc[:, ['temp', 'WBC', 'HeartRate', 'RR']] = test_features

    # Create sequences and labels for the new training, validation, and test data
    X_train, y_train = create_sequences_and_labels(new_train_data, sequence_length, num_hours_ahead)
    X_val, y_val = create_sequences_and_labels(val_data, sequence_length, num_hours_ahead)
    X_test, y_test = create_sequences_and_labels(test_data, sequence_length, num_hours_ahead)

    np.save('data/X_train.npy', X_train)
    np.save('data/y_train.npy', y_train)
    np.save('data/X_val.npy', X_val)
    np.save('data/y_val.npy', y_val)
    np.save('data/X_test.npy', X_test)
    np.save('data/y_test.npy', y_test)

    return 

