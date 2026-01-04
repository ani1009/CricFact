import re

def classify_claim(sentence):
    if re.search(r"\d+\s+runs|\d+\s+wickets", sentence.lower()):
        return "PLAYER_STATS"
    if "head-to-head" in sentence.lower():
        return "HEAD_TO_HEAD"
    if "won" in sentence.lower() and "final" in sentence.lower():
        return "MATCH_RESULT"
    return "GENERAL"
