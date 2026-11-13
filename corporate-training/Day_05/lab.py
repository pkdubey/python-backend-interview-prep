# Day 5 Lab — NLP Foundations
# pip install nltk textblob scikit-learn
import nltk
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
from textblob import TextBlob
import re

# ── SAMPLE REVIEWS ──────────────────────────────────────────────────────────
reviews = [
    ("Great product! Very fast delivery and excellent quality.", "positive"),
    ("Terrible experience. Product broke after 2 days.", "negative"),
    ("Amazing quality, will definitely buy again!", "positive"),
    ("Worst purchase ever. Complete waste of money.", "negative"),
    ("Good value for money. Satisfied with the purchase.", "positive"),
    ("Product not as described. Very disappointed.", "negative"),
    ("Fantastic! Exceeded my expectations.", "positive"),
    ("Poor quality. Returned immediately.", "negative"),
    ("Decent product for the price.", "positive"),
    ("Horrible customer service. Never buying again.", "negative"),
]

# ── SECTION 1: Text Cleaning ─────────────────────────────────────────────────
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)          # Remove punctuation
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]  # Remove stopwords
    tokens = [lemmatizer.lemmatize(t) for t in tokens]   # Lemmatize
    return tokens

print("=== Cleaned Tokens (first review) ===")
print(clean_text(reviews[0][0]))

# ── SECTION 2: Word Frequency ────────────────────────────────────────────────
neg_words = []
for text, label in reviews:
    if label == "negative":
        neg_words.extend(clean_text(text))

print("\n=== Top 10 Words in Negative Reviews ===")
for word, count in Counter(neg_words).most_common(10):
    print(f"  {word}: {count}")

# ── SECTION 3: Sentiment Analysis with TextBlob ──────────────────────────────
print("\n=== Sentiment Analysis ===")
correct = 0
for text, true_label in reviews:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    predicted = "positive" if polarity > 0 else "negative"
    match = "✅" if predicted == true_label else "❌"
    print(f"  {match} [{predicted}] {text[:50]}...")
    if predicted == true_label:
        correct += 1

accuracy = correct / len(reviews) * 100
print(f"\n  Accuracy: {accuracy:.0f}% ({correct}/{len(reviews)})")

# ── SECTION 4: TF-IDF ────────────────────────────────────────────────────────
from sklearn.feature_extraction.text import TfidfVectorizer

texts = [r[0] for r in reviews]
vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
tfidf_matrix = vectorizer.fit_transform(texts)

print("\n=== Top TF-IDF Features ===")
print(vectorizer.get_feature_names_out())
