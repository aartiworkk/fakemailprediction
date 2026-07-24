import streamlit as st
import joblib, re
from html.parser import HTMLParser

st.set_page_config(page_title="Fake Job Detector", layout="centered")
st.title("🔍 Fake Job Offer Detection AI")
st.write("Paste a job description to check if it's REAL or FAKE")

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__(); self.reset(); self.fed = []
    def handle_data(self, d): self.fed.append(d)
    def get_data(self): return ''.join(self.fed)

def strip_html(html):
    s = MLStripper()
    try:
        s.feed(html); return s.get_data()
    except Exception:
        return html

def clean_text(text):
    text = strip_html(str(text))
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'<[^>]+>', '', text).lower()
    return re.sub(r'\s+', ' ', text).strip()

@st.cache_resource
def load_lr():
    return joblib.load('tfidf.pkl'), joblib.load('lr_model.pkl')

user_input = st.text_area("Enter job description:", height=200)

if st.button("Check Job Posting", type="primary"):
    if not user_input.strip():
        st.warning("Please enter a job description!")
    else:
        cleaned = clean_text(user_input)
        tfidf, model = load_lr()
        vec = tfidf.transform([cleaned])
        prob = model.predict_proba(vec)[0][1]

        names = tfidf.get_feature_names_out()
        contrib = vec.toarray()[0] * model.coef_[0]
        reasons = [names[i] for i in contrib.argsort()[-5:][::-1] if contrib[i] > 0]

        if prob >= 0.5:
            st.error("🚨 FAKE JOB DETECTED")
        else:
            st.success("✅ LIKELY REAL JOB")

        st.metric("Fraud probability", f"{prob*100:.1f}%")
        st.progress(min(prob, 1.0))

        if reasons:
            st.write("**Terms that raised the fraud score:**")
            for r in reasons:
                st.write(f"• `{r}`")

st.divider()
st.caption("TF-IDF + Logistic Regression trained on EMSCAD "
           "(17,880 postings, 4.84% fraudulent). "
           "LSTM and DistilBERT trained and compared in the notebook.")
