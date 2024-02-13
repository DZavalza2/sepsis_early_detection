def LSTM_Model (X_train, y_train, X_val, y_val, X_test, y_test, num_epochs = 20, batch_size = 64):
    """
    This function takes in training, validation, and test data to return an LSTM model to predict 1 or 0 
    if a patient will have sepsis (num_hours_ahead) hours after. Function also prints out the test loss,
    test accuracy, and test recall.
    --------------
    Parameters:
    1. X_train: features training data, obtained in create_feature_labels.py
    2. y_train: labels training data, obtained in create_feature_labels.py
    3. X_val: features validation data, obtained in create_feature_labels.py
    4. y_val: labels validation data, obtained in create_feature_labels.py
    5. X_test: features test data, obtained in create_feature_labels.py
    6. y_test: labels test data, obtained in create_feature_labels.py
    7. num_epochs: numbers of epochs
    8. batch_size: models batch size
    """
    # Load Data
    X_train = np.load(X_train)
    y_train = np.load(y_train)
    X_val = np.load(X_val)
    y_val = np.load(y_val)
    X_test = np.load(X_test)
    y_test = np.load(y_test)

    # Model
    model = Sequential([
        LSTM(128, input_shape=(X_train.shape[1], X_train.shape[2]), return_sequences=True),
        Dropout(0.2),
        LSTM(128),
        Dropout(0.2),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', Recall()])

    for epoch in range(num_epochs):
        # Randomly sample indices from the majority class to match the minority class size
        sampled_majority_indices = np.random.choice(indices_class_0, size=len(indices_class_1), replace=False)
        
        # Combine sampled majority indices with all minority class indices
        combined_indices = np.concatenate([sampled_majority_indices, indices_class_1])
        
        # Shuffle the combined indices
        np.random.shuffle(combined_indices)

        # Use the combined indices to create the training dataset for this epoch
        X_train_epoch = X_train[combined_indices]
        y_train_epoch = y_train[combined_indices]

        # Train the model on this epoch's data
        model.fit(X_train_epoch, y_train_epoch, epochs=1, batch_size=batch_size, validation_data=(X_val, y_val))

    test_loss, test_accuracy, test_recall = model.evaluate(X_test, y_test)
    print(f"Test Loss: {test_loss}")
    print(f"Test Accuracy: {test_accuracy}")
    print(f"Test Recall: {test_recall}")

    return model