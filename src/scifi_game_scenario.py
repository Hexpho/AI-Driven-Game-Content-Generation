"""
Sci‑Fi Narrative Scenario: "Beyond the Known"
Lightweight demo aligned with the thesis.
"""
import random

PROMPTS = [
    "We are nearing the wormhole. Any readings?",
    "Is there intelligent life on this planet?",
    "Our shields are depleting. Options?",
    "Analyze this alien artifact.",
    "Tell me about quantum teleportation.",
    "We are low on fuel; energy sources?",
    "How does this starship's propulsion work?",
    "Have you seen a galaxy like this?",
    "First contact protocols?",
    "Any known cases of time travel?",
]

CUES = {
    "wormhole": "Sensors detect high curvature; recommend stabilizing the Einstein–Rosen aperture before entry.",
    "life": "Bio‑signatures present: methane fluctuations and irregular heat maps suggest microbial activity.",
    "shields": "Divert power from sub‑light engines; polarize hull plating; deploy decoy drones.",
    "artifact": "Emits low‑frequency EM pulses; handle in a Faraday enclosure; non‑terrestrial alloy detected.",
    "quantum": "Teleportation transfers quantum states, not matter; requires entanglement and classical channel.",
    "fuel": "Harvest deuterium from nearby ice rings; solar sail deployment is a secondary option.",
    "propulsion": "Hybrid ion drive with superconducting coils; maintain coil temperature below critical current.",
    "galaxy": "Spiral barred structure with dense core; anomaly density 1.7× sector median.",
    "contact": "Follow quarantine, non‑aggression, and math‑based greeting; avoid cultural contamination.",
    "time": "No verified macroscopic cases; localized dilations observed near extreme gravity wells.",
}

def generate_response(prompt: str) -> str:
    p = prompt.lower()
    for key, msg in CUES.items():
        if key in p:
            return msg
    return random.choice(list(CUES.values()))

def main():
    print("=== Sci‑Fi Scenario Demo ===")
    for prompt in PROMPTS:
        print(f"\nQ: {prompt}\nA: {generate_response(prompt)}")

if __name__ == "__main__":
    main()
