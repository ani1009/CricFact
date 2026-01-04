import re
import spacy

_nlp = None  # lazy-loaded


def get_nlp():
    global _nlp
    if _nlp is None:
        try:
            _nlp = spacy.load("en_core_web_sm")
        except Exception:
            # Safe fallback for Streamlit Cloud
            _nlp = spacy.blank("en")
    return _nlp


OPINION_WORDS = {
    "best", "greatest", "dominant", "impressive",
    "expected", "likely", "arguably", "superb"
}


def extract_sentences(text: str):
    nlp = get_nlp()
    return [sent.text.strip() for sent in nlp(text).sents]


def is_opinion(text: str) -> bool:
    t = text.lower()
    return any(word in t for word in OPINION_WORDS)


def has_number(text: str) -> bool:
    return bool(re.search(r"\d+", text))
