import spacy
import re

# Lazy-loaded spaCy model (Streamlit Cloud safe)
_nlp = None

def get_nlp():
    global _nlp
    if _nlp is None:
        try:
            _nlp = spacy.load("en_core_web_sm")
        except OSError:
            # Fallback: create blank English model
            _nlp = spacy.blank("en")
    return _nlp


OPINION_WORDS = [
    "best", "greatest", "dominant", "impressive",
    "expected", "likely", "arguably"
]


def extract_sentences(text):
    nlp = get_nlp()
    return [s.text.strip() for s in nlp(text).sents]


def is_opinion(text):
    return any(word in text.lower() for word in OPINION_WORDS)


def has_number(text):
    return bool(re.search(r"\d+", text))
