# 🏏 Cricket Fact Checker (AI-Assisted)

An **AI-assisted, editorial-grade cricket fact-checking application** built using **Python and Streamlit**, designed for **cricket writers, editors, and content teams**.

The app verifies cricket facts using **trusted public sources**:
- ESPNcricinfo
- Cricbuzz
- Sportskeeda

It supports **AI-generated articles**, **Word documents with tables**, and **PDF files**, and shows **ONLY incorrect facts** — no noise, no confusing scores, no unnecessary warnings.

---

## 🎯 Problem This App Solves

Cricket content often contains:
- Incorrect stats in AI-generated or human-written articles
- Errors hidden inside Word tables
- Time-consuming manual fact-checking
- False alarms from over-aggressive tools

This app is built with an **editor-first mindset**:
- It flags **only clearly incorrect facts**
- It stays **silent when unsure**
- It avoids false positives
- It supports **tables inside Word files**

---

## ✨ Key Features

### ✅ Writer-First Fact Checking
- Shows **ONLY incorrect cricket facts**
- No accuracy percentages or confusing labels
- Silent when facts are true or unverifiable
- Editorially safe behavior

### 🧠 Open-Source AI Integration
- Uses **`sentence-transformers/all-MPNet-base-v2`**
- Understands:
  - AI-generated articles (ChatGPT, Claude, etc.)
  - Humanized AI content
  - Long, polished editorial writing
- AI is used **only for language understanding**
- AI **never invents or decides facts**

### 📄 Multiple Input Methods
- Paste full article text
- Upload **Word (.docx)** files
- Upload **PDF (.pdf)** files

### 📊 Word Table Fact Checking (Major Highlight)
- Automatically reads **tables inside Word files**
- Converts each table row into factual sentences
- Verifies table data using trusted sources
- Identifies exactly:
  - Table number
  - Row number
  - Column name
- Displays table errors clearly in UI and reports

### 📌 Clear Output
- ❌ Lists only incorrect facts
- ✅ Shows “Safe to publish” when no issues are found
- No “Needs fact check” or yellow warnings

### 📥 Exportable Reports
- Download **PDF** report (incorrect facts only)
- Download **Word (.docx)** report
- Table errors included with row & column references

### 🎨 Clean UI & Animations
- Loading spinner during processing
- Progress bar while checking
- Simple, editor-friendly interface

---

## 🧠 How the App Works (Simple Flow)


---

## 🧱 Tech Stack

- Python 3.9+
- Streamlit (UI)
- spaCy (sentence processing)
- Sentence Transformers – MPNet (AI understanding)
- Requests + BeautifulSoup (source scraping)
- python-docx (Word & table parsing)
- PyPDF2 (PDF text extraction)
- ReportLab (PDF report generation)

---

## 📁 Project Structure

cricket_fact_checker/
│
├── app.py # Main Streamlit app
├── ai_helper.py # Open-source AI (MPNet)
├── utils.py # Text utilities
├── verifier.py # Fact verification logic
├── exporter.py # PDF & Word report export
├── file_reader.py # Word/PDF + table reader
│
└── scrapers/
├── init.py
├── espn.py
├── cricbuzz.py
└── sportskeeda.py


---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/cricket-fact-checker.git
cd cricket-fact-checker
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Download spaCy Model
python -m spacy download en_core_web_sm

5️⃣ Run the App
streamlit run app.py


Open in browser:

http://localhost:8501
