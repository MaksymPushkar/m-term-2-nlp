# Lab 6 — TF-IDF + Logistic Regression baseline

## 1. Classification task

Класифікація SMS повідомлень на spam / ham.

## 2. Data split

Використано stratified train/test split (80/20) з random_state=42.

## 3. Baseline 1

TF-IDF (word n-grams (1,1)) + Logistic Regression

- Accuracy: 0.973
- Macro-F1: 0.936

## 4. Baseline 2

TF-IDF (word n-grams (1,2)) + Logistic Regression + class_weight="balanced"

- Accuracy: 0.982
- Macro-F1: 0.961

## 5. Comparison

Baseline 2 показав кращі результати завдяки використанню біграм (більше контексту)
та балансуванню класів.

## 6. Confusion Matrix insights

Модель добре класифікує більшість прикладів, але іноді помиляється на коротких або
неоднозначних повідомленнях.

## 7. Top features

Для класу spam характерні слова типу:
free, call, txt, win, prize

Для класу ham:
ok, go, come, got, know

Ознаки виглядають логічними, підозрілих токенів не виявлено.

## 8. Error analysis

Проаналізовано 10+ помилок.

Основні категорії:

- overlap класів
- short text (недостатньо контексту)
- rare vocabulary

## 9. Most frequent errors

Найчастіше:

- короткі повідомлення
- нечіткий контекст між spam і ham

## 10. What to fix next

- додати більше даних
- покращити preprocessing
- використовувати більш складні моделі (наприклад, SVM або BERT)
