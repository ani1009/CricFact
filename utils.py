import spacy
import re

nlp = spacy.load("en_core_web_sm")

OPINION_WORDS = [
    "best", "greatest", "dominant", "impressive",
    "expected", "likely", "arguably"
]

def extract_sentences(text):
    return [s.text.strip() for s in nlp(text).sents]

def is_opinion(text):
    return any(w in text.lower() for w in OPINION_WORDS)

def has_number(text):
    return bool(re.search(r"\d+", text))
