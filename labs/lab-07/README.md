Task
Classification of procurement descriptions.

Baseline
TF-IDF + Logistic Regression from Lab6.

Tested models
Linear SVM with word ngrams.
Linear SVM with char ngrams.
Linear SVM with class_weight balanced.

Imbalance
Dataset contains class imbalance.

Threshold
Custom threshold selected based on PR curve analysis.

Best model
Linear SVM with class_weight balanced.

Future work
Try combining word and char features and perform hyperparameter tuning.
