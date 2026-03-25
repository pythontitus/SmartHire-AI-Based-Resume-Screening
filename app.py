import gradio as gr
import pandas as pd
import spacy
import re
import os
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load NLP model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

def extract_text(file_path):
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""
    return text

def parse_resume(text):
    email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    phone = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
    doc = nlp(text[:300])
    name = "Not Detected"
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break
    return {
        "name": name,
        "email": email[0] if email else "N/A",
        "phone": phone[0] if phone else "N/A"
    }

def check_plagiarism(texts):
    if len(texts) < 2: return ["✅ Low"] * len(texts)
    tfidf = TfidfVectorizer().fit_transform(texts)
    matrix = cosine_similarity(tfidf)
    risks = []
    for i in range(len(texts)):
        sim_scores = [matrix[i][j] for j in range(len(texts)) if i != j]
        max_score = max(sim_scores) if sim_scores else 0
        if max_score > 0.8: risks.append(f"🚩 High ({int(max_score*100)}%)")
        elif max_score > 0.5: risks.append(f"⚠️ Mod ({int(max_score*100)}%)")
        else: risks.append("✅ Low")
    return risks

def start_screening(jd, files):
    if not jd or not files:
        return pd.DataFrame(), pd.DataFrame()

    resumes_list = []
    for f in files:
        raw_text = extract_text(f.name)
        info = parse_resume(raw_text)
        resumes_list.append({
            "name": info["name"],
            "email": info["email"],
            "phone": info["phone"],
            "text": raw_text,
            "filename": os.path.basename(f.name),
            "path": f.name
        })

    all_texts = [jd] + [r['text'] for r in resumes_list]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    plagiarism_results = check_plagiarism([r['text'] for r in resumes_list])

    df = pd.DataFrame({
        "Candidate Name": [r['name'] for r in resumes_list],
        "Contact Email": [r['email'] for r in resumes_list],
        "Phone": [r['phone'] for r in resumes_list],
        "Match Score (%)": [round(s * 100, 1) for s in scores],
        "Plagiarism": plagiarism_results,
        "Original_File": [r['filename'] for r in resumes_list],
        "Hidden_Path": [r['path'] for r in resumes_list] 
    }).sort_values(by="Match Score (%)", ascending=False)

    return df, df.drop(columns=["Hidden_Path"])

# UI Layout
with gr.Blocks(theme=gr.themes.Soft(), title="Smart Hire AI") as demo:
    gr.Markdown("# 🚀 Smart Hire: AI Multi-Feature Screener")
    
    with gr.Row():
        with gr.Column(scale=1):
            jd_input = gr.Textbox(label="Job Description", lines=7, placeholder="Paste requirements...")
            file_input = gr.File(label="Upload Resumes (PDF)", file_count="multiple")
            run_btn = gr.Button("⚡ Analyze & Rank", variant="primary")

        with gr.Column(scale=2):
            full_data_state = gr.State()
            results_table = gr.Dataframe(interactive=False)

    pdf_view = gr.File(label="Quick Preview")

    run_btn.click(fn=start_screening, inputs=[jd_input, file_input], outputs=[full_data_state, results_table])
    
    results_table.select(lambda df_full, evt: df_full.iloc[evt.index[0]]["Hidden_Path"], [full_data_state], pdf_view)

if __name__ == "__main__":
    demo.launch()