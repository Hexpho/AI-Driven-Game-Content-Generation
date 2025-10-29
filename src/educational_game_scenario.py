"""
Educational Game Scenario: "Digital Realm of Knowledge"
Lightweight demo aligned with the thesis.
"""
import random

PROMPTS = [
    "What is a variable in Python?",
    "How do loops work?",
    "Explain functions simply.",
    "Why do I get syntax errors?",
    "List vs tuple?",
    "What are dictionaries?",
    "What are classes and objects?",
    "Tips for handling errors?",
    "What is a try/except block?",
]

CANNED = {
    "variable": "A variable is a named reference to a value in memory. Use '=' to assign.",
    "loops": "Use 'for' for iteration over sequences; use 'while' for condition-based repetition.",
    "functions": "Functions group reusable logic: define with 'def', return results with 'return'.",
    "syntax": "Check colons, indentation, quotes, and unmatched parentheses/brackets.",
    "list tuple": "Lists are mutable [ ], tuples are immutable ( ). Choose based on mutability.",
    "dictionaries": "Dictionaries store key→value pairs. Create with { } and access via dict[key].",
    "classes": "Classes define new types; objects are instances. Use __init__ for initialization.",
    "errors": "Wrap risky code in try/except; log messages; fail fast in development.",
    "try": "try/except catches exceptions; 'finally' runs always; 'else' runs if no exception.",
}

def generate_response(prompt: str) -> str:
    p = prompt.lower()
    for key, msg in CANNED.items():
        if all(k in p for k in key.split()):
            return msg
    return random.choice(list(CANNED.values()))

def main():
    print("=== Educational Scenario Demo ===")
    for prompt in PROMPTS:
        print(f"\nQ: {prompt}\nA: {generate_response(prompt)}")

if __name__ == "__main__":
    main()
