def cost_matrix(confusion_matrix, fp_cost, fn_cost):
    """
    Creates a cost matrix where a weight is assigned to both the False Positives and False Negatives. Also, returns
    the total cost using both the confusion matrix and the cost_matrix.
    ----------------------------
    Parameters:
    1. confusion_matrix: 2d list obtained by confusion matrix when running the lstm model
    2. fp_cost: Weight of the false positive cost (should be lower than fn_cost)
    3. fn_cost: Weight of the false negative cost (should be higher than fp_cost)
    ----------------------------
    Example:
    cm = [[102665, 36426], [24106, 48217]]
    fp_cost = 10
    fn_cost = 3
    total_cost, cost_mat = cost_matrix(cm, fp_cost, fn_cost)
    # total_cost output -> 436578
    # cost_matrix output -> [[0, 10], [3, 0]]
    
    """
    TN, FP = confusion_matrix[0][0], confusion_matrix[0][1]
    FN, TP = confusion_matrix[1][0], confusion_matrix[1][1]
    cost = FP * fp_cost + FN * fn_cost
    
    return cost, [[0, fp_cost], [fn_cost, 0]]