# Fake Job Offer Detection using NLP & Transformers

This project aims to detect fraudulent job postings using traditional ML, Deep Learning (LSTM), and Transformer-based models (DistilBERT). It includes preprocessing, model comparison, and a deployment-ready Streamlit application.

---

## Features
- End-to-end NLP pipeline (cleaning, preprocessing, tokenization)
- ML baseline: TF-IDF + Logistic Regression
- Deep Learning model: LSTM
- Transformer model: DistilBERT (fine-tuned)
- Streamlit app for real-time predictions
- Comparison of ML/DL/Transformer models
- Deployment-ready folder structure

---

## Project Structure

```
fake-job-offer-detection/
│
├── app.py                     # Streamlit UI
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignore cache & model files
├── LICENSE                    # MIT license
├── Fake_Job_Offer_Detection_Full_Report.docx  # Full report
│
├── notebook/
│   └── Fake_Job_Detection.ipynb  # Kaggle Notebook
│
├── model/                     # Fine-tuned DistilBERT Model
│   ├── config.json
│   ├── pytorch_model.bin
│   └── tokenizer.json
│
└── assets/                    # Images / diagrams
    ├── diagram.png
    └── screenshots.png
```

---

## Models Implemented
### 1️⃣ Logistic Regression (TF-IDF)
- Baseline model  
- Fast, interpretable  
- Limited contextual understanding  

### 2️⃣ LSTM
- Captures sequential text patterns  
- Better performance than TF-IDF  

### 3️⃣ DistilBERT (Transformer)
- Best accuracy and F1-score  
- Learns deep contextual patterns  
- Final deployed model  

---

## Installation

```
git clone https://github.com/yourusername/fake-job-offer-detection.git
cd fake-job-offer-detection
pip install -r requirements.txt
```

---

## Run the Streamlit App

```
streamlit run app.py
```

---

## Dataset
**Fake Job Posting Dataset — Kaggle**  
https://www.kaggle.com/shivamb/real-or-fake-fake-jobposting-prediction

---

## Results
| Model | Accuracy | F1-Score |
|-------|----------|----------|
| Logistic Regression | Medium | Medium |
| LSTM | High | High |
| **DistilBERT** | **Best** | **Best** |

---

## Requirements
See `requirements.txt`

---

## Author  
**Aarti**  
B.Tech CSE (AI), IGDTUW  
