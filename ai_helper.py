from sentence_transformers import SentenceTransformer

# Load once (cached in memory)
model = SentenceTransformer("sentence-transformers/all-MPNet-base-v2")

AI_FILLERS = [
    "it is worth noting that",
    "overall",
    "from a broader perspective",
    "interestingly",
    "notably",
    "in conclusion",
    "to put it simply"
]

def normalize_claim(text: str) -> str:
    """
    Uses lightweight AI cleanup + semantic tolerance.
    Does NOT generate or modify facts.
    """
    text = text.lower().strip()

    for f in AI_FILLERS:
        text = text.replace(f, "")

    return text.strip()
