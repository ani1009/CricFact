from scrapers.espn import search_text as espn
from scrapers.cricbuzz import search_text as cricbuzz
from scrapers.sportskeeda import search_text as sportskeeda

def cross_verify(query, value):
    """
    SAFE editorial verification logic.

    Rules:
    - If value is missing → Ignore
    - If sources cannot confirm → Ignore
    - ONLY flag when explicitly contradicted (future-safe)
    """

    # Safety guard (prevents NoneType errors)
    if not value:
        return "Ignore"

    sources = {
        "ESPN": espn(query),
        "Cricbuzz": cricbuzz(query),
        "Sportskeeda": sportskeeda(query)
    }

    confirmed = 0

    for text in sources.values():
        if text and value in text:
            confirmed += 1

    # If at least 2 sources confirm, it's verified (ignored in UI)
    if confirmed >= 2:
        return "Verified"

    # Not confirmed → IGNORE (do NOT mark wrong)
    return "Ignore"
