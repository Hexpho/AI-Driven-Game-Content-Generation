"""
Metrics & Reporting (stub):
Placeholders that reflect the thesis' evaluation pipeline.
"""
from collections import Counter
import math

def coherence_rate(responses):
    # very simple repetition heuristic: unique/total tokens ratio
    tokens = " ".join(responses).split()
    if not tokens:
        return 100.0
    unique_ratio = len(set(tokens)) / max(1, len(tokens))
    # Map to a percentage-like score
    return round(50 + 50 * unique_ratio, 2)

def context_relevance(responses, keywords):
    hits = 0
    for r in responses:
        if any(k.lower() in r.lower() for k in keywords):
            hits += 1
    return round(100 * hits / max(1, len(responses)), 2)

def demo():
    rs = ["A variable stores a value", "Use for loops for iteration", "Functions encapsulate logic"]
    print("Coherence Rate:", coherence_rate(rs), "%")
    print("Context Relevance (['variable','loop','function']):", context_relevance(rs, ['variable','loop','function']), "%")

if __name__ == "__main__":
    demo()
