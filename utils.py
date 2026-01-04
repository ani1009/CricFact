import re
import spacy

# spaCy model will be loaded lazily (Cloud-safe)
_nlp = None


def get_nlp():
    global _nlp
    if _nlp is None:
        try:
            _nlp = spacy.load("en_core_web_sm")
        except Exception:
            # Absolute safe fallback for Streamlit Cloud
            _nlp = spacy.blank("en")
    return _nlp


OPINION_WORDS = {
    "best", "greatest", "dominant", "impressive",
    "expected", "likely", "arguably", "excellent",
    "superb", "fantastic"
}


def extract_sentences(text: str):
    """
    Split text into sentences safely.
    Works even if spaCy model is unavailable.
    """
    nlp = get_nlp()
    return [sent.text.strip() for sent in nlp(text).sents]


def is_opinion(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in OPINION_WORDS)


def has_number(text: str) -> bool:
    return bool(re.search(r"\d+", text))
