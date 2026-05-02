# 🧠 Sentiment Analysis — NLP Portfolio Project

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![NLP](https://img.shields.io/badge/NLP-TextBlob%20%7C%20VADER-green?style=flat-square)
![Visualization](https://img.shields.io/badge/Visualization-Tableau%20%7C%20Power%20BI-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)
![Colab](https://img.shields.io/badge/Run%20on-Google%20Colab-yellow?style=flat-square&logo=googlecolab)

> Analyzing customer product reviews using NLP techniques (TextBlob + VADER) to classify sentiments as **Positive**, **Negative**, or **Neutral** — with interactive dashboards in Tableau and Power BI.

---

## 📌 Project Overview

Customer reviews contain valuable insights for businesses. This project builds an **end-to-end Sentiment Analysis pipeline** that:

- Processes raw customer reviews
- Applies two NLP models (TextBlob & VADER)
- Generates a clean CSV dataset for BI tools
- Visualizes sentiment trends across products and time

---

## 🎯 Key Features

| Feature | Details |
|---|---|
| **Dual NLP Models** | TextBlob (lexicon-based) + VADER (social-media optimized) |
| **Multi-Product Analysis** | Laptop, Headphones, Mouse, Keyboard, Monitor |
| **Time-Series Trends** | Sentiment tracked over months |
| **BI-Ready Output** | CSV compatible with Tableau & Power BI |
| **Python Charts** | 4-panel dashboard via Matplotlib |

---

## 🗂️ Project Structure

```
sentiment-analysis/
│
├── sentiment_analysis.py     # Main Python script
├── requirements.txt          # Dependencies
├── sentiment_results.csv     # Output dataset (Tableau/Power BI input)
├── sentiment_dashboard.png   # Auto-generated Python chart
└── README.md                 # Project documentation
```

---

## 📊 Sample Output

```
Review                                          Sentiment   Score    Rating
──────────────────────────────────────────────────────────────────────────
"This product is absolutely amazing!"           Positive    +0.871     5 ⭐
"Terrible quality. Broke after 2 days."         Negative    -0.827     1 ⭐
"It's okay, nothing special."                   Neutral     -0.046     3 ⭐
"Excellent build quality and fast delivery!"    Positive    +0.777     5 ⭐
"Very disappointed. Not as described."          Negative    -0.526     2 ⭐
```

**Overall Results (20 Reviews):**
- ✅ Positive: 9 reviews (45%)
- ❌ Negative: 9 reviews (45%)
- ➖ Neutral: 2 reviews (10%)

---

## 🛠️ Tech Stack

```
Python 3.10+
├── textblob          → Lexicon-based sentiment scoring
├── vaderSentiment    → VADER model (optimized for reviews)
├── pandas            → Data manipulation & CSV export
└── matplotlib        → Chart generation

BI Tools
├── Tableau Desktop   → Interactive dashboards
└── Microsoft Power BI → DAX measures & slicers
```

---
## 📚 What I Learned

- Difference between **rule-based** (TextBlob) and **lexicon-based** (VADER) NLP models
- How to structure a **data pipeline**: raw text → analysis → visualization
- Connecting Python outputs to **enterprise BI tools** (Tableau, Power BI)
- Writing **DAX measures** for calculated KPIs in Power BI

---

## 🔮 Future Improvements

- [ ] Add **real Amazon/Twitter dataset** via API
- [ ] Train a **custom ML model** (Logistic Regression / BERT)
- [ ] Build a **Streamlit web app** for live review input
- [ ] Add **Urdu language** sentiment support

---

## 👩‍💻 Author

**[Maryam Saif]**  
Data Science Student
📧 [Maryamcheema736@gmail.com]  
🔗 [[LinkedIn Profile URL](https://www.linkedin.com/in/maryam-saif-110859231)]  
💻 [[GitHub Profile URL](https://github.com/saifmaryam)]

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*⭐ If you found this helpful, please star the repository!*
