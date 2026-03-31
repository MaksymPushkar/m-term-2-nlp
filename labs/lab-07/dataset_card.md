Dataset: Public procurement text classification

Classes show moderate imbalance where minority classes contain fewer examples.

Text data contains noise such as spelling variations, abbreviations and short descriptions.

Character n-grams were tested to handle spelling variation and noisy text.

Results showed that char-ngrams slightly improved recall for minority classes.

The most difficult class was small procurement categories with short descriptions.

Balanced class weights improved macro-F1 by increasing recall on minority classes.

Precision-recall trade-off was handled by selecting a threshold favouring balanced precision and recall.
