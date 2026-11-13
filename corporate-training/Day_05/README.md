# Day 5 — NLP Foundations
**Vibe:** "How computers read text — and why it's harder than it sounds."

---

## 🗣️ How to Open This Day

> "Computers are great with numbers. But text? 'I love this product' and 'This product is amazing' mean the same thing — but to a computer, they're completely different strings. Today we teach computers to understand language."

---

## 🧠 Concepts & Human-Language Explanations

### Tokenization
**Say this:** "Tokenization is chopping a sentence into pieces. Like cutting a pizza into slices — the pizza is still the same pizza, just easier to handle."

```python
from nltk.tokenize import word_tokenize
text = "The quick brown fox jumps over the lazy dog"
tokens = word_tokenize(text)
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
```

### Stopwords
**Say this:** "Words like 'the', 'is', 'a', 'an' carry no meaning. They're noise. We remove them so the computer focuses on the important words."

```python
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
filtered = [w for w in tokens if w.lower() not in stop_words]
# ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog']
```

### Stemming vs Lemmatization
**Say this:** "Both reduce words to their root form. 'Running', 'runs', 'ran' → all mean 'run'. Stemming is fast but crude (chops the end off). Lemmatization is smarter (uses a dictionary)."

```python
# Stemming: fast, rough
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemmer.stem("running")   # "run"
stemmer.stem("studies")   # "studi" ← crude!

# Lemmatization: slower, accurate
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("studies")  # "study" ← correct
```

### TF-IDF — "How Important is This Word?"
**Say this:** "TF-IDF answers: 'Is this word important in THIS document, compared to all other documents?' The word 'the' appears everywhere — low score. The word 'transformer' appears only in AI papers — high score."

- **TF (Term Frequency):** How often does this word appear in THIS document?
- **IDF (Inverse Document Frequency):** How rare is this word across ALL documents?
- **TF-IDF = TF × IDF** — High score = important and unique word

### Word Embeddings — "Words on a Map"
**Say this:** "Instead of treating words as text, we convert them to numbers (vectors). Words with similar meanings end up close together on a giant map. 'King' is close to 'Queen'. 'Dog' is close to 'Cat'. This is how AI understands meaning."

```
King - Man + Woman ≈ Queen   ← Famous example
```

**Why this matters:** "This is the foundation of everything we'll do in Days 6-14. Every LLM, every RAG system — it all starts with embeddings."

### Sentiment Analysis — "Is This Review Positive or Negative?"
**Say this:** "This is the 'Hello World' of NLP. Every e-commerce company, every bank, every hospital uses this to understand customer feedback at scale."

---

## 💻 Live Coding Demo

**Scenario:** "You work at an e-commerce company. You have 1000 customer reviews. Your manager wants to know: what percentage are positive? What are customers complaining about?"

See `lab.py`.

---

## 🏋️ Hands-on Challenge

Given a list of 20 customer reviews (provided in lab):
1. Clean the text (lowercase, remove punctuation, stopwords)
2. Find the top 10 most frequent words in negative reviews
3. Build a simple sentiment classifier using TextBlob
4. Print: "X% positive, Y% negative reviews"

---

## 📝 Daily Recap Questions

1. "Why do we remove stopwords?"
2. "What's the difference between stemming and lemmatization?"
3. "In your company, where could sentiment analysis be useful?"

**Key takeaway:** "NLP is the bridge between human language and machine understanding. Everything from chatbots to search engines to spam filters uses these concepts."

---

## 🔗 Connection to Tomorrow

> "Today we processed text manually — rule-based, step by step. Tomorrow we'll see how modern AI (Transformers/LLMs) does this automatically, at a much deeper level of understanding."
