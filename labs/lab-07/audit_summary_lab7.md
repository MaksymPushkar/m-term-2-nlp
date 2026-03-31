Task
Text classification of public procurement descriptions.

Baseline from Lab6
TF-IDF + Logistic Regression

Tested models

1. Logistic Regression baseline
2. Linear SVM word ngrams
3. Linear SVM char ngrams
4. Linear SVM with class_weight balanced

Best model
Linear SVM with balanced class weights

Accuracy: ~0.86
Macro F1: ~0.82

Char-ngrams
Provided small improvement for noisy text and spelling variation.

Class imbalance
Using class_weight="balanced" improved recall for minority classes.

Threshold
Custom threshold was chosen to balance precision and recall.

Common errors

1. Short ambiguous texts
2. Overlapping procurement categories
3. Lack of context in description.
