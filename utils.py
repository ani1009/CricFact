import re
import spacy

_nlp = None  # lazy-loaded, Streamlit Cloud safe


def get_nlp():
    global _nlp
    if _nlp is None:
        try:
            # Try loading full model
            _nlp = spacy.load("en_core_web_sm")
        except Exception:
            # Fallback: blank English + sentencizer
            _nlp = spacy.blank("en")
            if "sentencizer" not in _nlp.pipe_names:
                _nlp.add_pipe("sentencizer")
    return _nlp


OPINION_WORDS = {
    "best", "greatest", "dominant", "impressive",
    "expected", "likely", "arguably", "excellent",
    "superb", "fantastic"
}


def extract_sentences(text: str):
    """
    Safely split text into sentences.
    Works both with full spaCy model and blank fallback.
    """
    if not text or not text.strip():
        return []

    nlp = get_nlp()
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents if sent.text.strip()]


def is_opinion(text: str) -> bool:
    return any(word in text.lower() for word in OPINION_WORDS)


def has_number(text: str) -> bool:
    return bool(re.search(r"\d+", text))
