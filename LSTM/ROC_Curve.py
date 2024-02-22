def AUROC_Curve(model, X_test, y_test):
    """
    Function which outputs an AUROC Curve based on the model obtained from LSTM_Model.py.

    --------------------------
    1. model - model obtained by running LSTM_Model.py 
    2. X_test - features test data, obtained in create_feature_labels.py
    3. y_test - labels test data, obtained in create_feature_labels.py
    """
    y_probabilities = model.predict(X_test).ravel()

    # Calculate AUROC
    auroc = roc_auc_score(y_test, y_probabilities)

    # Calculate ROC curve
    fpr, tpr, thresholds = roc_curve(y_test, y_probabilities)

    plt.figure(figsize=(10, 10)) 
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {auroc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()