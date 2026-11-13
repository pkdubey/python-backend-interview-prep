# Day 5 Theory — NLP Foundations
## "Teaching computers to read"

---

## 1. What is NLP?

NLP = Natural Language Processing = Teaching computers to understand human language.

**The problem:** Computers understand numbers. Not text.

"I love this product" — to a computer, this is just a sequence of characters: I, space, l, o, v, e...

NLP's job is to extract meaning from that text.

**Real life use cases:**
- Gmail's spam filter — "Is this email spam or not?"
- Google Translate — one language to another
- Alexa/Siri — understanding voice commands
- Analyzing customer reviews — positive or negative?
- Chatbots — answering customer questions

---

## 2. Text Processing Pipeline

Steps to extract useful information from raw text:

```
Raw Text
   ↓
Cleaning (lowercase, remove punctuation)
   ↓
Tokenization (split into words)
   ↓
Remove Stopwords (remove useless words)
   ↓
Stemming/Lemmatization (get root form)
   ↓
Feature Extraction (convert to numbers)
   ↓
Model / Analysis
```

Let's understand each step.

---

## 3. Tokenization — "Slicing a Pizza"

Tokenization = Splitting a sentence into words.

Like slicing a pizza — the pizza is the same, it's just easier to handle in slices.

```python
from nltk.tokenize import word_tokenize

text = "The quick brown fox jumps over the lazy dog"
tokens = word_tokenize(text)
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
```

**Sentence tokenization** also exists:
```python
from nltk.tokenize import sent_tokenize

para = "I love Python. It is amazing. Everyone should learn it."
sentences = sent_tokenize(para)
# ['I love Python.', 'It is amazing.', 'Everyone should learn it.']
```

---

## 4. Stopwords — "Remove the Noise"

Stopwords = Words that carry no meaning.

"the", "is", "a", "an", "in", "on", "at" — these appear in every sentence. Remove them and the important words stand out more clearly.

```python
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
# {'the', 'is', 'a', 'an', 'in', 'on', 'at', 'to', 'for', ...}

tokens = ['The', 'product', 'is', 'very', 'good', 'and', 'fast']
filtered = [w for w in tokens if w.lower() not in stop_words]
# ['product', 'very', 'good', 'fast']
```

**Before:** "The product is very good and fast delivery"
**After:** "product good fast delivery"

The second version is much more useful for a computer.

---

## 5. Stemming vs Lemmatization — "Finding the Root Word"

Both reduce words to their root form.

"running", "runs", "ran" — all mean "run". We need to teach the computer this.

**Stemming** — Fast but rough. Chops the end off:
```python
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

stemmer.stem("running")    # "run" ✅
stemmer.stem("studies")    # "studi" ❌ — crude!
stemmer.stem("better")     # "better" ❌ — should be "good"
```

**Lemmatization** — Slower but accurate. Uses a dictionary:
```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

lemmatizer.lemmatize("studies")           # "study" ✅
lemmatizer.lemmatize("running", pos="v")  # "run" ✅
lemmatizer.lemmatize("better", pos="a")   # "good" ✅
```

**When to use which?**
- Speed matters, slight inaccuracy is okay → Stemming
- Accuracy is important → Lemmatization

---

## 6. TF-IDF — "How Important is This Word?"

TF-IDF answers: "How important is this word in this document?"

**TF (Term Frequency):** How often does this word appear in THIS document?
```
TF = (word count in document) / (total words in document)
```

**IDF (Inverse Document Frequency):** How rare is this word across ALL documents?
```
IDF = log(total documents / documents containing this word)
```

If a word appears in all documents → IDF is low → importance is low
If a word appears in only a few documents → IDF is high → importance is high

**TF-IDF = TF × IDF**

**Example:**
- Word "the" → TF high (in every sentence), IDF low (in all documents) → TF-IDF low
- Word "transformer" → TF medium, IDF high (only in AI papers) → TF-IDF high

```python
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "Python is great for data science",
    "Python is used in machine learning",
    "Data science uses machine learning",
]

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(docs)
print(vectorizer.get_feature_names_out())
```

---

## 7. Word Embeddings — "Plotting Words on a Map"

This concept is critical — all of modern AI is built on this.

**Problem with simple approach:**
"King" and "Queen" — both are royalty, they're related. But to a computer, they're just different strings.

**Solution: Embeddings**

Convert every word into a list of numbers (a vector). Similar words get similar numbers.

```
"King"  → [0.2, 0.8, 0.1, 0.9, ...]
"Queen" → [0.2, 0.7, 0.9, 0.8, ...]  ← similar numbers!
"Dog"   → [0.9, 0.1, 0.3, 0.2, ...]  ← very different numbers
```

**The famous example:**
```
King - Man + Woman ≈ Queen
```

With numbers:
```
[0.2, 0.8, 0.1] - [0.3, 0.5, 0.2] + [0.3, 0.6, 0.8] ≈ [0.2, 0.9, 0.7]
                                                          ↑ Queen's numbers!
```

**Why this matters:**
RAG, LLMs, semantic search — everything from Day 6 onwards is built on embeddings. This is the foundation.

---

## 8. Sentiment Analysis — "Positive or Negative?"

Sentiment analysis = Understanding the mood of text.

**Use cases:**
- Customer reviews: "What are people saying about this product?"
- Social media: "Is the brand sentiment positive or negative?"
- Employee feedback: "How is team morale?"

**Simple approach — TextBlob:**
```python
from textblob import TextBlob

reviews = [
    "This product is amazing! Best purchase ever.",
    "Terrible quality. Complete waste of money.",
    "It's okay, nothing special.",
]

for review in reviews:
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    # polarity: -1 (very negative) to +1 (very positive)

    if polarity > 0.1:
        sentiment = "POSITIVE 😊"
    elif polarity < -0.1:
        sentiment = "NEGATIVE 😞"
    else:
        sentiment = "NEUTRAL 😐"

    print(f"{sentiment}: {review}")
```

---

## 9. Named Entity Recognition (NER) — "Find the Important Things"

NER = Automatically extracting names, places, dates, organizations from text.

```python
import spacy
nlp = spacy.load("en_core_web_sm")

text = "Pavan Kumar Dubey joined TechCorp in Bangalore on January 15, 2024."
doc = nlp(text)

for entity in doc.ents:
    print(f"{entity.text} → {entity.label_}")

# Pavan Kumar Dubey → PERSON
# TechCorp → ORG
# Bangalore → GPE (Geo-Political Entity)
# January 15, 2024 → DATE
```

**Real use case:** Automatically extract company names from news articles, find dates in contracts, identify people in emails.

---

## 10. Traditional NLP vs Modern AI (Preview)

What we learned today is "traditional NLP" — rule-based, step-by-step.

**Traditional NLP:**
- Manually tokenize, clean, stem
- Build features with TF-IDF
- Train a simple ML model
- Accuracy: 70-80%

**Modern AI (LLMs — from tomorrow):**
- One line: "Tell me the sentiment of this review"
- The model handles everything internally
- Accuracy: 90%+

**So why did we learn traditional NLP?**
- To understand the foundation — LLMs do the same things internally
- For when an LLM isn't available (offline, cost constraints)
- For debugging — when AI gives a wrong answer, you can understand why

---

## Summary

| Concept | What it does | Example |
|---------|-------------|---------|
| Tokenization | Sentence → words | "Hello World" → ["Hello", "World"] |
| Stopwords | Remove meaningless words | Remove "the", "is", "a" |
| Stemming | Fast root word | "running" → "run" |
| Lemmatization | Accurate root word | "better" → "good" |
| TF-IDF | Word importance score | "transformer" scores higher than "the" |
| Embeddings | Words → numbers | Similar words → similar numbers |
| Sentiment | Positive/Negative/Neutral | Review analysis |
| NER | Extract names/places/dates | "Bangalore" → GPE |

**Tomorrow:** No need to do all this manually — LLMs do it automatically. Generative AI!
