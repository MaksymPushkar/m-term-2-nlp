# Leakage Risk Report — Lab 5

## Split strategy

We used stratified random split with seed 42 to maintain similar class distribution across train, validation and test datasets.

## Split statistics

Train: 80%  
Validation: 10%  
Test: 10%

Class distribution across splits is approximately equal.

## Leakage checks

Exact duplicates  
train∩test = 0  
train∩val = 0  
val∩test = 0

Near duplicates  
TF-IDF + cosine similarity threshold 0.95 detected 2 similar pairs.

Template leakage  
No template leakage detected.

Group leakage  
Not applicable.

Time leakage  
Not applicable.

## Remaining risks

- possible near duplicate texts
- possible class imbalance in future data
- domain drift

## Mitigation

- deduplication
- dataset expansion
- monitoring class distribution
