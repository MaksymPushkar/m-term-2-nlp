# IE Policy — Lab 4 (Rule-based Information Extraction)

## Extracted Field Types

This module extracts three types of structured information from text:

- DATE
- AMOUNT
- PHONE

The approach is rule-based and uses regular expressions with small dictionaries.

---

# 1. DATE

## Definition

Any calendar date mentioned in the format:

- DD.MM.YYYY
- DD/MM/YYYY
- D.M.YYYY

Example:
12.05.2024

## Normalization

Output format:

YYYY-MM-DD

Example:

12.05.2024 → 2024-05-12

If parsing fails:

raw_date is stored and parsed_date = None.

## Not considered DATE

- year alone (2024)
- numbers without separators
- numeric identifiers

## Edge cases

1. 01.01.2023
2. 31/12/2024
3. 29.02.2024 (leap year)
4. 1.5.2022
5. invalid date 32.01.2024

---

# 2. AMOUNT

## Definition

Monetary value with currency indicator.

Supported currencies:

- грн
- ₴
- UAH
- USD
- $
- EUR
- €

Examples:

5000 грн  
100 USD  
200.50 €

## Normalization

Output fields:

value (float)  
currency (UAH/USD/EUR)

Example:

5000 грн → value=5000.0, currency=UAH

## Not considered AMOUNT

- percentages (100%)
- plain numbers without currency
- numeric identifiers

## Edge cases

1. 5000 грн
2. 100 USD
3. 200€
4. 100.50 грн
5. 100%

---

# 3. PHONE

## Definition

Ukrainian phone numbers.

Supported formats:

+380XXXXXXXXX  
0XXXXXXXXX

Examples:

+380671234567  
0671234567

## Normalization

Output format:

+380XXXXXXXXX

Example:

0671234567 → +380671234567

## Not considered PHONE

- short numeric sequences
- order numbers
- IDs

## Edge cases

1. +380671234567
2. 0671234567
3. +380501234567
4. 0501234567
5. 067-123-4567
