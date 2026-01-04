import streamlit as st
import time
import re

from ai_helper import normalize_claim
from utils import extract_sentences, is_opinion, has_number
from verifier import cross_verify
from exporter import export_pdf, export_word
from file_reader import read_word, read_pdf

st.set_page_config(page_title="Cricket Fact Checker", layout="wide")

st.title("🏏 CrickFact")
st.caption("AI-assisted verification using ESPNcricinfo, Cricbuzz & Sportskeeda")

# ---------------- INPUT MODE ---------------- #
input_mode = st.radio(
    "Choose input method",
    ["Upload Word File", "Paste Article", "Upload PDF File"],
    horizontal=True
)

data = []

if input_mode == "Upload Word File":
    file = st.file_uploader("Upload .docx", type=["docx"])
    if file:
        with st.spinner("Reading Word file and tables…"):
            time.sleep(1)
            data = read_word(file)
        st.success("Word file loaded (text + tables)")

elif input_mode == "Paste Article":
    text = st.text_area("Paste article", height=280)
    if text.strip():
        data = [{"text": s, "source": "paragraph"} for s in extract_sentences(text)]

elif input_mode == "Upload PDF File":
    file = st.file_uploader("Upload .pdf", type=["pdf"])
    if file:
        with st.spinner("Reading PDF…"):
            time.sleep(1)
            data = read_pdf(file)
        st.warning("PDF tables may not be fully supported")

# ---------------- VERIFY ---------------- #
if st.button("🚀 Verify Facts"):
    if not data:
        st.warning("Please provide content first.")
    else:
        incorrect = []
        progress = st.progress(0)

        for i, item in enumerate(data):
            progress.progress((i + 1) / len(data))

            # AI normalization + cleanup
            text = normalize_claim(item["text"])

            # Ignore opinions or non-factual lines
            if is_opinion(text) or not has_number(text):
                continue

            # SAFE number extraction (fixes NoneType bug)
            match = re.search(r"\d+", text)
            if not match:
                continue

            value = match.group()
            status = cross_verify(text, value)

            # ONLY collect clearly incorrect facts
            if status == "Fact Incorrect":
                incorrect.append(item)

        progress.empty()
        st.markdown("---")

        if not incorrect:
            st.success("✅ No incorrect facts found. Article is safe to publish.")
        else:
            st.error("❌ Incorrect Facts Found")

            for e in incorrect:
                if e.get("source") == "table":
                    st.error(
                        f"Table {e['table']} → Row {e['row']} → Column '{e['column']}'\n\n{e['text']}"
                    )
                else:
                    st.error(e["text"])

            # -------- EXPORT -------- #
            st.markdown("### 📄 Download Report (Incorrect Facts Only)")
            col1, col2 = st.columns(2)

            with col1:
                pdf = export_pdf(incorrect)
                with open(pdf, "rb") as f:
                    st.download_button("Download PDF", f, file_name=pdf)

            with col2:
                docx = export_word(incorrect)
                with open(docx, "rb") as f:
                    st.download_button("Download Word", f, file_name=docx)
