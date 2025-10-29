# Developing a Model for AI-Driven Game Design Process

This repository contains the bachelor thesis project by **Baturalp Bilen Burmaoglu** (Riga Technical University, 2024).  
It explores how Artificial Intelligence (AI) can be integrated with game design rules to improve narrative and level design coherence.

## 🎮 Scenarios
- **Educational Game:** *Digital Realm of Knowledge* – interactive Python tutoring.
- **Sci‑Fi Narrative:** *Beyond the Known* – space‑exploration dialogues with an AI companion.

## 🧠 Tech Stack
- Python, PyTorch, HuggingFace Transformers (GPT‑2)
- Sentence‑BERT (semantic similarity)
- ROUGE, Precision/Recall/F1, MCC
- pandas, matplotlib, scikit‑learn

## ✨ What’s Inside
- `src/` – runnable reference scripts for each scenario + metrics helpers
- `thesis/` – full thesis PDF and original notebook
- `results/` – example outputs / tables (sample)
- `requirements.txt` – dependencies
- `.gitignore` – common ignores

##  Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Educational scenario
python src/educational_game_scenario.py

# Sci‑Fi scenario
python src/scifi_game_scenario.py
```

> **Note:**   If the notebook preview does not render properly on GitHub, you can still open it in **Google Colab**.  
Click the file name above → **“Raw”** → copy the URL of the raw file,  
then open [Google Colab](https://colab.research.google.com/),  
go to **File → Open notebook → GitHub**, and paste that URL to view the full notebook interactively.
>The scripts are lightweight, self‑contained demos aligned with the thesis. 
> For full experiments (parameter sweeps, figures, tables), use the notebook in `thesis/Batu_Bachelor_Thesis.ipynb`.

## 📚 Citation
Burmaoglu, Baturalp Bilen (2024). *Developing a Model for AI‑Driven Game Design Process.* Riga Technical University.

## 📄 License
MIT
