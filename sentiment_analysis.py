"""
======================================================
  SENTIMENT ANALYSIS PROJECT - NLP Portfolio Project
  By: [Aapka Naam Yahan Likho]
  Tools: Python, TextBlob, VADER, Pandas, Matplotlib
======================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime, timedelta
import random
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────
# STEP 1: SAMPLE DATA (Amazon Reviews)
# ─────────────────────────────────────
reviews_data = [
    {"review": "This product is absolutely amazing! Best purchase ever.", "product": "Laptop", "rating": 5},
    {"review": "Terrible quality. Broke after 2 days. Complete waste of money.", "product": "Headphones", "rating": 1},
    {"review": "It's okay, nothing special. Does the job but nothing more.", "product": "Mouse", "rating": 3},
    {"review": "Excellent build quality and fast delivery. Highly recommend!", "product": "Keyboard", "rating": 5},
    {"review": "Very disappointed. Not as described in the listing.", "product": "Laptop", "rating": 2},
    {"review": "Great value for money. Works perfectly for my needs.", "product": "Monitor", "rating": 4},
    {"review": "Worst customer service ever. Product stopped working after a week.", "product": "Headphones", "rating": 1},
    {"review": "Decent product. Shipping was fast. Would buy again.", "product": "Mouse", "rating": 4},
    {"review": "Absolutely love this! Exceeded my expectations completely.", "product": "Keyboard", "rating": 5},
    {"review": "Average product. Not bad but not great either.", "product": "Monitor", "rating": 3},
    {"review": "Super happy with this purchase! Fast shipping and great quality.", "product": "Laptop", "rating": 5},
    {"review": "Do not buy this. Complete scam. Returned immediately.", "product": "Headphones", "rating": 1},
    {"review": "Good product but slightly overpriced for what you get.", "product": "Mouse", "rating": 3},
    {"review": "Fantastic! Exactly what I needed. Perfect condition.", "product": "Keyboard", "rating": 5},
    {"review": "Battery life is terrible. Very frustrating to use.", "product": "Monitor", "rating": 2},
    {"review": "Works as expected. No issues so far after 3 months.", "product": "Laptop", "rating": 4},
    {"review": "Amazing sound quality! Very impressed with the performance.", "product": "Headphones", "rating": 5},
    {"review": "Stopped working after one month. Really let down by this.", "product": "Mouse", "rating": 2},
    {"review": "The build quality is outstanding. Worth every penny.", "product": "Keyboard", "rating": 5},
    {"review": "Not what I expected. Poor packaging and missing parts.", "product": "Monitor", "rating": 2},
]

# Add random dates for time-series analysis
start_date = datetime(2024, 1, 1)
for i, review in enumerate(reviews_data):
    review['date'] = (start_date + timedelta(days=i*18)).strftime('%Y-%m-%d')

df = pd.DataFrame(reviews_data)

# ─────────────────────────────────────
# STEP 2: SENTIMENT ANALYSIS
# ─────────────────────────────────────
print("=" * 50)
print("   SENTIMENT ANALYSIS - PROCESSING...")
print("=" * 50)

# Method 1: TextBlob
def textblob_sentiment(text):
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity
    if score > 0.05:
        return 'Positive', round(score, 3)
    elif score < -0.05:
        return 'Negative', round(score, 3)
    else:
        return 'Neutral', round(score, 3)

# Method 2: VADER (better for social media / reviews)
analyzer = SentimentIntensityAnalyzer()

def vader_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        label = 'Positive'
    elif compound <= -0.05:
        label = 'Negative'
    else:
        label = 'Neutral'
    return label, round(compound, 3)

# Apply both methods
df[['TB_Sentiment', 'TB_Score']] = df['review'].apply(
    lambda x: pd.Series(textblob_sentiment(x))
)
df[['VADER_Sentiment', 'VADER_Score']] = df['review'].apply(
    lambda x: pd.Series(vader_sentiment(x))
)

# Final sentiment (using VADER - more accurate for reviews)
df['Final_Sentiment'] = df['VADER_Sentiment']
df['Confidence'] = df['VADER_Score'].abs().apply(
    lambda x: 'High' if x > 0.5 else ('Medium' if x > 0.2 else 'Low')
)

print("\n✅ Sample Results:")
print(df[['review', 'Final_Sentiment', 'VADER_Score', 'rating']].head(5).to_string())

# ─────────────────────────────────────
# STEP 3: SAVE CSV (for Tableau/Power BI)
# ─────────────────────────────────────
output_file = 'sentiment_results.csv'
df.to_csv(output_file, index=False)
print(f"\n✅ CSV saved: {output_file}")
print(f"   Total reviews analyzed: {len(df)}")
print(f"   Positive: {len(df[df['Final_Sentiment']=='Positive'])}")
print(f"   Negative: {len(df[df['Final_Sentiment']=='Negative'])}")
print(f"   Neutral:  {len(df[df['Final_Sentiment']=='Neutral'])}")

# ─────────────────────────────────────
# STEP 4: VISUALIZATIONS (Python Charts)
# ─────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Sentiment Analysis Dashboard', fontsize=16, fontweight='bold', y=0.98)

colors = {'Positive': '#2ecc71', 'Negative': '#e74c3c', 'Neutral': '#f39c12'}

# Chart 1: Overall Sentiment Pie Chart
sentiment_counts = df['Final_Sentiment'].value_counts()
ax1 = axes[0, 0]
wedge_colors = [colors[s] for s in sentiment_counts.index]
ax1.pie(sentiment_counts, labels=sentiment_counts.index, colors=wedge_colors,
        autopct='%1.1f%%', startangle=90, textprops={'fontsize': 11})
ax1.set_title('Overall Sentiment Distribution', fontweight='bold')

# Chart 2: Sentiment by Product (Bar Chart)
ax2 = axes[0, 1]
product_sentiment = df.groupby(['product', 'Final_Sentiment']).size().unstack(fill_value=0)
product_sentiment.plot(kind='bar', ax=ax2,
                       color=[colors.get(c, '#95a5a6') for c in product_sentiment.columns],
                       edgecolor='white', width=0.7)
ax2.set_title('Sentiment by Product', fontweight='bold')
ax2.set_xlabel('')
ax2.set_ylabel('Number of Reviews')
ax2.legend(title='Sentiment', loc='upper right')
ax2.tick_params(axis='x', rotation=30)

# Chart 3: Sentiment Score Distribution
ax3 = axes[1, 0]
pos_scores = df[df['Final_Sentiment'] == 'Positive']['VADER_Score']
neg_scores = df[df['Final_Sentiment'] == 'Negative']['VADER_Score']
neu_scores = df[df['Final_Sentiment'] == 'Neutral']['VADER_Score']
ax3.hist(pos_scores, bins=8, color='#2ecc71', alpha=0.7, label='Positive')
ax3.hist(neg_scores, bins=8, color='#e74c3c', alpha=0.7, label='Negative')
ax3.hist(neu_scores, bins=8, color='#f39c12', alpha=0.7, label='Neutral')
ax3.set_title('Sentiment Score Distribution', fontweight='bold')
ax3.set_xlabel('VADER Compound Score (-1 to +1)')
ax3.set_ylabel('Frequency')
ax3.legend()
ax3.axvline(x=0, color='black', linestyle='--', alpha=0.5)

# Chart 4: Average Rating vs Sentiment
ax4 = axes[1, 1]
avg_rating = df.groupby('Final_Sentiment')['rating'].mean().reindex(['Positive', 'Neutral', 'Negative'])
bar_colors = [colors[s] for s in avg_rating.index]
bars = ax4.bar(avg_rating.index, avg_rating.values, color=bar_colors, edgecolor='white', width=0.5)
ax4.set_title('Average Rating by Sentiment', fontweight='bold')
ax4.set_ylabel('Average Star Rating')
ax4.set_ylim(0, 5.5)
for bar, val in zip(bars, avg_rating.values):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
             f'{val:.1f}⭐', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('sentiment_dashboard.png', dpi=150, bbox_inches='tight')
print("\n✅ Chart saved: sentiment_dashboard.png")

plt.show()
print("\n" + "=" * 50)
print("   PROJECT COMPLETE! Ready for Tableau/Power BI")
print("   Load 'sentiment_results.csv' in Tableau or Power BI")
print("=" * 50)
