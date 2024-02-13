def confusion_matrix(model, X_test, y_test):
    """
    Using your model obtained from LSTM_Model.py, this function will create a confusion matrix so we can see
    what number of patients are being labeled accuractly, False Negatives, and False Positives.
    -----------------------
    Parameters:
    1. model - model obtained by running LSTM_Model.py 
    2. X_test - features test data, obtained in create_feature_labels.py
    3. y_test - labels test data, obtained in create_feature_labels.py
    """

    predictions = model.predict(X_test)
    predicted_classes = (predictions >= 0.5).astype(int).flatten()

    conf_matrix = confusion_matrix(y_test, predicted_classes)
    print(conf_matrix)

    # convert original tensor matrix to array
    conf_matrix_array = np.array(conf_matrix)

    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix_array, annot=True, fmt="d", cmap='Blues', cbar=False, 
                xticklabels=['Predicted Negative', 'Predicted Positive'],
                yticklabels=['Actual Negative', 'Actual Positive'])

    plt.title('Confusion Matrix')
    plt.show()


