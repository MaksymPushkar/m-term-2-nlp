import re
from typing import List, Dict

URL_RE = re.compile(r'https?://\\S+')
EMAIL_RE = re.compile(r'\\S+@\\S+')
PHONE_RE = re.compile(r'\\+?\\d[\\d\\s\\-\\(\\)]{7,}')
MULTISPACE_RE = re.compile(r'\\s+')

UA_ABBREVIATIONS = {"м.", "вул.", "р.", "т.д.", "ім."}

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = text.replace("\\n", " ").replace("\\t", " ")
    text = MULTISPACE_RE.sub(" ", text)
    return text.strip()

def normalize_text(text: str) -> str:
    text = text.replace("’", "'").replace("`", "'")
    text = text.replace("–", "-").replace("—", "-")
    text = text.replace("«", '"').replace("»", '"')
    return text

def mask_pii(text: str) -> str:
    text = URL_RE.sub("<URL>", text)
    text = EMAIL_RE.sub("<EMAIL>", text)
    text = PHONE_RE.sub("<PHONE>", text)
    return text

SENT_SPLIT_RE = re.compile(r'(?<=[.!?])\\s+(?=[А-ЯA-Z])')

def sentence_split(text: str) -> List[str]:
    parts = SENT_SPLIT_RE.split(text)
    merged = []
    for part in parts:
        if merged and any(merged[-1].endswith(abbr) for abbr in UA_ABBREVIATIONS):
            merged[-1] += " " + part
        else:
            merged.append(part)
    return merged

def preprocess(text: str) -> Dict:
    clean = clean_text(text)
    norm = normalize_text(clean)
    masked = mask_pii(norm)
    sentences = sentence_split(masked)

    return {
        "clean_text": masked,
        "sentences": sentences
    }
