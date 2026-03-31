import numpy as np

def evaluate_thresholds(scores, threshold):

    preds = (scores > threshold).astype(int)

    return preds