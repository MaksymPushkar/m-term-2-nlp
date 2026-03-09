import re
from datetime import datetime

currencies = {
    "грн": "UAH",
    "₴": "UAH",
    "uah": "UAH",
    "$": "USD",
    "usd": "USD",
    "€": "EUR",
    "eur": "EUR"
}

date_regex = r'\b(\d{1,2})[./](\d{1,2})[./](\d{4})\b'
amount_regex = r'\b(\d+[.,]?\d*)\s?(грн|₴|uah|usd|\$|eur|€)\b'
phone_regex = r'\+?380\d{9}|\b0\d{9}\b'


def extract_dates(text):

    results = []

    for m in re.finditer(date_regex, text):

        day, month, year = m.groups()

        try:
            parsed = datetime(int(year), int(month), int(day))
            norm = parsed.strftime("%Y-%m-%d")
        except:
            norm = None

        results.append({
            "field_type": "DATE",
            "value": norm,
            "raw": m.group(),
            "start_char": m.start(),
            "end_char": m.end(),
            "method": "regex_date"
        })

    return results


def extract_amounts(text):

    results = []

    for m in re.finditer(amount_regex, text.lower()):

        value, cur = m.groups()

        value = float(value.replace(",", "."))

        currency = currencies.get(cur, "UNKNOWN")

        results.append({
            "field_type": "AMOUNT",
            "value": value,
            "currency": currency,
            "start_char": m.start(),
            "end_char": m.end(),
            "method": "regex_amount"
        })

    return results


def normalize_phone(phone):

    phone = phone.replace(" ", "").replace("-", "")

    if phone.startswith("0"):
        phone = "+38" + phone

    if not phone.startswith("+"):
        phone = "+" + phone

    return phone


def extract_phones(text):

    results = []

    for m in re.finditer(phone_regex, text):

        raw = m.group()

        results.append({
            "field_type": "PHONE",
            "value": normalize_phone(raw),
            "raw": raw,
            "start_char": m.start(),
            "end_char": m.end(),
            "method": "regex_phone"
        })

    return results


def extract_all(text):

    results = []

    results += extract_dates(text)
    results += extract_amounts(text)
    results += extract_phones(text)

    return results