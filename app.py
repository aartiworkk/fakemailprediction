import streamlit as st
import re
from html.parser import HTMLParser

st.set_page_config(page_title="Fake Job Detector", layout="centered")

st.title("🔍 Fake Job Offer Detection AI")
st.write("Paste a job description to check if it's REAL or FAKE")

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_html(html):
    s = MLStripper()
    try:
        s.feed(html)
        return s.get_data()
    except:
        return html

def clean_text(text):
    text = str(text)
    text = strip_html(text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def predict_fraud(text):
    fraud_keywords = [
        'earn money fast', 'make $', 'work from home easy', 'no experience needed',
        'no interview', 'guaranteed', 'easy money', 'quick cash', 'registration fee',
        'send money', 'upfront payment', 'pyramid', 'mlm', 'limited time',
        'act now', 'call immediately', 'contact us', 'sketchy', 'too good to be true',
        'unlimited income', 'no qualifications', 'risk free', '$5000', '$10000',
        'per week', 'per day', 'recruitment fee', 'training cost'
    ]
    
    text_lower = text.lower()
    fraud_score = 0
    
    for keyword in fraud_keywords:
        if keyword in text_lower:
            fraud_score += 1
    
    missing_details = 0
    if '@' not in text:
        missing_details += 1
    if 'http' not in text and 'www' not in text:
        missing_details += 1
    if '$' not in text:
        missing_details += 1
    
    if fraud_score > 2 or (fraud_score > 0 and missing_details > 1):
        confidence = min(95, 50 + (fraud_score * 15))
        return True, confidence
    elif fraud_score > 0:
        confidence = 30 + (fraud_score * 10)
        return True, confidence
    else:
        confidence = 15
        return False, confidence

user_input = st.text_area("Enter job description:", height=200)

if st.button("Check Job Posting", type="primary"):
    if user_input:
        cleaned = clean_text(user_input)
        is_fake, confidence = predict_fraud(cleaned)
        
        if is_fake:
            st.error(f"🚨 FAKE JOB DETECTED!")
            st.metric("Confidence", f"{confidence:.1f}%")
            st.write("**Why it might be fake:**")
            
            fraud_indicators = []
            text_lower = cleaned.lower()
            
            if any(kw in text_lower for kw in ['earn money fast', 'make $', 'guaranteed']):
                fraud_indicators.append("• Unrealistic earning promises")
            if any(kw in text_lower for kw in ['no experience', 'no qualifications']):
                fraud_indicators.append("• No experience required (red flag)")
            if any(kw in text_lower for kw in ['registration fee', 'send money', 'upfront']):
                fraud_indicators.append("• Asks for upfront payment")
            if any(kw in text_lower for kw in ['act now', 'limited time', 'immediately']):
                fraud_indicators.append("• Creates artificial urgency")
            if '@' not in cleaned and 'http' not in cleaned:
                fraud_indicators.append("• Missing legitimate contact info")
            
            if fraud_indicators:
                for indicator in fraud_indicators:
                    st.write(indicator)
        else:
            st.success(f"✅ LIKELY REAL JOB")
            st.metric("Confidence", f"{100 - confidence:.1f}%")
            st.write("This job posting appears legitimate based on standard criteria.")
    else:
        st.warning("Please enter a job description!")