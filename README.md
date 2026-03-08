# 🚀 Smart Hire — AI Resume Screener

> An intelligent, multi-feature resume screening tool built with **Python**, **spaCy**, **scikit-learn**, and **Gradio**.  
> Rank candidates against a job description, detect plagiarism between resumes, and auto-extract contact info — all in one click.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 **JD Match Scoring** | TF-IDF cosine similarity ranks every resume against your job description |
| 🚩 **Plagiarism Detection** | Cross-compares all resumes and flags suspiciously similar submissions |
| 🔍 **Contact Extraction** | Automatically extracts candidate name (spaCy NER), email, and phone |
| 👁️ **Resume Preview** | Click any row in the leaderboard to preview that PDF inline |
| 🏆 **Ranked Leaderboard** | Sorted table with scores, plagiarism risk, and extracted contact info |

---

## 📸 Screenshot

```
┌─────────────────────────────────────────────────────────────────────┐
│  🚀 Smart Hire — AI Resume Screener                                 │
│                                                                     │
│  [Job Description .............]  │  🏆 Candidate Leaderboard      │
│  [Upload Resumes (PDF)       ]   │  Rank | Name | Score | Risk    │
│  [⚡ Analyze & Rank          ]   │   1   | Jane |  87%  |  ✅ Low │
│                                  │   2   | Alex |  74%  |  ⚠️ Mod │
│  ─────────────────────────────── │   3   | Sam  |  61%  |  ✅ Low │
│  Resume Preview (click a row ↑)  │                                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

- **[Gradio](https://gradio.app/)** — Interactive web UI
- **[spaCy](https://spacy.io/)** — NLP for name entity recognition
- **[scikit-learn](https://scikit-learn.org/)** — TF-IDF vectorization & cosine similarity
- **[PyPDF2](https://pypdf2.readthedocs.io/)** — PDF text extraction
- **[pandas](https://pandas.pydata.org/)** — Data manipulation

---

## ⚙️ Setup & Installation

### Option A — Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/smart-hire.git
cd smart-hire

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download spaCy language model
python -m spacy download en_core_web_sm

# 4. Launch the app
python smart_hire.py
```

The app will open at **http://localhost:7860** in your browser.

---

### Option B — Run on Google Colab

1. Open [Google Colab](https://colab.research.google.com/)
2. Create a new notebook and paste:

```python
!pip install gradio spacy PyPDF2 scikit-learn pandas
!python -m spacy download en_core_web_sm

# Paste the contents of smart_hire.py here, then run
```

3. Gradio will generate a public share link automatically.

---

## 🚀 How to Use

1. **Paste** your job description into the text box on the left.
2. **Upload** one or more candidate resumes as PDF files.
3. Click **⚡ Analyze & Rank**.
4. View the ranked leaderboard — scores, plagiarism flags, and extracted contact info appear instantly.
5. **Click any row** to preview that candidate's resume PDF below the table.

---

## 📁 Project Structure

```
smart-hire/
├── smart_hire.py       # Main application (all-in-one)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 🔬 How It Works

### Matching Score
Resumes and the job description are converted into **TF-IDF vectors**. Cosine similarity between each resume vector and the JD vector produces a match percentage (0–100%).

### Plagiarism Detection
All resumes are cross-compared pairwise using TF-IDF cosine similarity:
- **> 80%** similarity → 🚩 High risk
- **50–80%** similarity → ⚠️ Moderate risk
- **< 50%** similarity → ✅ Low risk

### Contact Extraction
- **Name** — spaCy's `en_core_web_sm` NER scans the first 300 characters for `PERSON` entities
- **Email** — Regex pattern matching standard email formats
- **Phone** — Regex pattern matching international and local phone number formats

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

---

## 👤 Author

Made with ❤️ — feel free to star ⭐ the repo if you find it useful!
