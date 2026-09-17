# Module 5: LLM, Hugging Face, Celery, Redis, AWS — Complete Interview Preparation

[← Back to Index](README.md) | [← Previous: Module 4](module-4-mysql-sql.md)

> **Note:** Ye module Google, Microsoft, Amazon jaise product-based companies ke liye prepare kiya gaya hai. Yahan sirf questions nahi — **thinking process** bhi explain kiya hai. Har answer ko natural language mein rakha hai, jaise ek 5.5 years experienced Python backend developer interview mein bolta hai. AI/ML questions mein honesty important hai — jo kiya hai wahi bolo, fake mat karo.

---

# PART 1: AI MODERATION PROJECT (Q81–Q90)

---

**Q81. Explain your AI-based content moderation project.**

"This was one of my most challenging and interesting projects. Let me explain it step by step.

**The Problem:**
Neighborshook is a hyperlocal platform where users post content — text, comments, community posts. With growing user base, manually moderating content became impossible. We needed an automated system to flag harmful content.

**The Solution:**
We built an AI-powered content moderation system. The goal was to automatically identify:
- Toxicity
- Spam
- Harassment
- Policy violations

**The Architecture:**
- Backend was built using Laravel and Django REST APIs.
- When a user submitted content, the API validated it and stored the initial record.
- The content was passed to an NLP pipeline.
- We integrated Hugging Face Transformers — mainly DistilBERT — for toxicity detection and text classification.
- The moderation result was stored in MySQL.
- APIs exposed the results to the admin moderation dashboard.
- We also had rule-based checks along with AI-based classification to improve reliability.

**My Role:**
My main contribution was backend development. I worked on:
- Django/Laravel APIs
- Hugging Face integration
- NLP pipeline
- Database handling
- Error handling
- Moderation dashboard APIs

I didn't train the model from scratch — we used pretrained models and adapted them."

**Follow-up: What was the biggest challenge?**

"The biggest challenge was balancing accuracy with speed. DistilBERT was a good trade-off — it's smaller and faster than BERT but still maintains good accuracy. We also had to handle false positives and false negatives, so we combined AI output with rule-based checks and manual review for low-confidence cases."

**Follow-up: How did you handle multilingual content?**

"The platform was primarily in English, so DistilBERT worked well. For multilingual support, we would have needed multilingual models like mBERT or XLM-R. But since the requirement was English, we didn't need that."

---

**Q82. Why did you use Hugging Face instead of building your own model?**

"This is an important question. Let me explain the reasoning.

**Why not build from scratch?**
1. **Data** — Training a transformer model requires millions of labeled examples. We didn't have that.
2. **Compute** — Training requires GPUs and significant time. Not practical for our team.
3. **Expertise** — We are backend developers, not ML researchers.
4. **Time** — Building from scratch would take months.

**Why Hugging Face?**
1. **Pretrained models** — Ready to use. We just needed to integrate.
2. **Community** — Thousands of models available for different tasks.
3. **Documentation** — Excellent docs and examples.
4. **Flexibility** — We could choose the right model for our use case.

We focused on:
- Model selection — choosing DistilBERT for speed vs accuracy
- Integration — making it work with our Django/Laravel backend
- Response handling — parsing model output
- Application-level workflow — combining AI with rule-based checks

**Follow-up: Did you fine-tune the model?**

"We didn't fine-tune DistilBERT extensively. We used it as-is with some prompt engineering and post-processing. For our use case, the pretrained model's toxicity detection was good enough. Fine-tuning would have required labeled data and more resources.

If we had more data, fine-tuning would have improved accuracy. But for MVP, pretrained was sufficient."

**Follow-up: What is the difference between fine-tuning and using pretrained?**

"**Pretrained** — model is trained on general data. You use it directly.
**Fine-tuned** — model is further trained on your specific data. Better for domain-specific tasks.

For example, DistilBERT pretrained on Wikipedia might not understand slang. Fine-tuning on social media data would help."

---

**Q83. What is an LLM?**

"LLM stands for Large Language Model. It's a deep learning model trained on a huge amount of text data to understand and generate human-like language.

**Key characteristics:**
1. **Large** — billions of parameters.
2. **Language** — understands and generates natural language.
3. **Model** — trained on massive datasets.

**What they can do:**
- Text classification
- Summarization
- Question answering
- Translation
- Content generation
- Code generation
- Sentiment analysis

**Examples:**
- GPT-4 (OpenAI)
- Gemini (Google)
- Claude (Anthropic)
- Llama (Meta)
- Mistral (Mistral AI)

In my work, I've used transformer-based models through Hugging Face for NLP tasks like toxicity detection."

**Follow-up: How is LLM different from traditional ML?**

"Traditional ML models are task-specific. You train a model for one task — like spam detection or sentiment analysis. LLMs are general-purpose. One model can do multiple tasks.

Also, traditional ML needs feature engineering. LLMs learn features automatically from data. And LLMs are much larger — billions of parameters vs thousands in traditional ML."

**Follow-up: What are the limitations of LLMs?**

"1. **Hallucination** — can generate incorrect information confidently.
2. **Cost** — running large models is expensive.
3. **Latency** — can be slow for real-time applications.
4. **Context window** — limited to a certain number of tokens.
5. **Bias** — inherits biases from training data.
6. **No real-time knowledge** — trained up to a cutoff date."

---

**Q84. Explain Transformer architecture.**

"Transformer is a deep learning architecture introduced in the paper 'Attention Is All You Need' in 2017. It revolutionized NLP.

**Key components:**

1. **Encoder** — processes input sequence.
2. **Decoder** — generates output sequence.
3. **Self-Attention** — allows the model to focus on relevant parts of input.
4. **Multi-Head Attention** — multiple attention mechanisms in parallel.
5. **Feed-Forward Networks** — process each position independently.
6. **Positional Encoding** — adds information about word order.

**Why it's important:**
- Unlike RNNs, transformers process sequences in parallel.
- This makes training faster.
- And allows handling longer contexts.

**Architecture diagram:**
```
Input → Encoder (Self-Attention + Feed-Forward) → Decoder → Output
```

In my moderation project, DistilBERT is based on the Transformer encoder. It processes text and outputs classification."

**Follow-up: What is the difference between Transformer and RNN?**

"**RNN** — processes sequences sequentially. Slow. Limited context.
**Transformer** — processes sequences in parallel. Fast. Long context.

RNNs struggle with long-range dependencies. Transformers handle them well because of self-attention."

**Follow-up: What is positional encoding?**

"Since transformers process all positions in parallel, they don't know the order of words. Positional encoding adds information about position. It's added to the input embeddings."

---

**Q85. What is Self-Attention?**

"Self-attention allows a model to understand which words are important in relation to other words in the same sentence.

**Example:**
'The animal didn't cross the street because it was too tired.'

What does 'it' refer to? The animal or the street? Self-attention helps the model understand that 'it' refers to 'the animal' because of the context.

**How it works:**
1. Each word is converted to a query, key, and value vector.
2. Query of one word is compared with keys of all words.
3. Attention scores are calculated.
4. Values are weighted by attention scores.
5. Output is a weighted sum.

**Formula:**
```
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
```

**Why it's important:**
- Captures long-range dependencies.
- Parallelizable.
- Interpretable — we can see what the model attends to."

**Follow-up: What is Multi-Head Attention?**

"Multi-Head Attention runs multiple self-attention mechanisms in parallel. Each head learns different relationships. Outputs are concatenated and projected.

For example:
- One head might focus on syntax.
- Another on semantics.
- Another on coreference.

This gives the model a richer understanding."

---

**Q86. Difference between BERT and GPT?**

"This is a common interview question. Let me explain clearly.

| Feature | BERT | GPT |
|---------|------|-----|
| **Architecture** | Encoder-only | Decoder-only |
| **Training** | Masked language modeling | Causal language modeling |
| **Direction** | Bidirectional | Unidirectional (left-to-right) |
| **Use case** | Understanding tasks | Generation tasks |
| **Examples** | Classification, NER, QA | Text generation, chat, code |
| **Models** | BERT, DistilBERT, RoBERTa | GPT-3, GPT-4, Llama |

**BERT** — reads the entire sentence at once. Good for classification, sentiment analysis, named entity recognition.

**GPT** — generates text one token at a time. Good for chatbots, content generation, code generation.

In my moderation project, I used BERT-based models (DistilBERT) because I needed classification, not generation."

**Follow-up: Can you use BERT for generation?**

"Not directly. BERT is trained for masked language modeling — predicting masked words. It doesn't generate text sequentially. But you can use it for tasks like text infilling or as an encoder in encoder-decoder models."

**Follow-up: What is the difference between BERT and RoBERTa?**

"RoBERTa is an optimized version of BERT. It:
1. Trains longer
2. Uses more data
3. Removes next sentence prediction
4. Uses dynamic masking

RoBERTa generally performs better than BERT on most tasks."

---

**Q87. Difference between Encoder-only and Decoder-only models?**

"**Encoder-only models:**
- Examples: BERT, DistilBERT, RoBERTa
- Process entire input bidirectionally
- Good for understanding tasks
- Use cases: Classification, NER, QA, embeddings

**Decoder-only models:**
- Examples: GPT, Llama, Mistral
- Process input left-to-right
- Good for generation tasks
- Use cases: Text generation, chat, code

**Encoder-decoder models:**
- Examples: T5, BART
- Encoder processes input, decoder generates output
- Good for sequence-to-sequence tasks
- Use cases: Translation, summarization

**In my work:**
I used DistilBERT (encoder-only) for toxicity classification. If I needed to generate moderated content, I would have used a decoder-only model."

**Follow-up: Which one is better?**

"Depends on the task:
- Classification → Encoder-only
- Generation → Decoder-only
- Translation/Summarization → Encoder-decoder

There's no 'better' — it's about the right tool for the job."

---

**Q88. What is DistilBERT and why did you use it?**

"DistilBERT is a smaller, faster, and lighter version of BERT. It's created through knowledge distillation — a technique where a smaller model learns from a larger model.

**Key facts:**
- 40% smaller than BERT
- 60% faster
- Retains 97% of BERT's performance

**How it works:**
1. Take a pretrained BERT (teacher).
2. Train a smaller model (student) to mimic BERT's outputs.
3. Student learns to generalize like the teacher.

**Why I used it:**
For our moderation system, we needed:
1. **Fast inference** — users were waiting for moderation results.
2. **Lower cost** — running BERT was expensive.
3. **Good accuracy** — 97% of BERT's performance was sufficient.

DistilBERT was the perfect trade-off between speed and accuracy."

**Follow-up: What is knowledge distillation?**

"Knowledge distillation is a technique where a smaller model (student) is trained to mimic a larger model (teacher). The student learns from the teacher's outputs — not just the correct labels, but the soft probabilities.

This allows the smaller model to capture the teacher's knowledge more efficiently than training from scratch."

**Follow-up: Would you use DistilBERT for all tasks?**

"No. For tasks where accuracy is critical — like medical diagnosis or legal document analysis — I'd use full BERT or a larger model. For real-time applications where speed matters, DistilBERT is better."

---

**Q89. How did you handle inconsistent model responses?**

"This is a critical production question. NLP models can be inconsistent — same input can give different outputs.

**Our approach:**

1. **Strict classification categories**
   - We defined clear categories: toxic, spam, harassment, safe.
   - The model had to choose one.

2. **Confidence thresholds**
   - If confidence was below a threshold, we marked it for manual review.
   - This prevented low-confidence auto-moderation.

3. **Validation on the backend**
   - We validated model output before saving.
   - If output was unexpected, we logged it and handled gracefully.

4. **Exception handling**
   - Wrapped model calls in try/except.
   - Fallback logic if model failed.

5. **Combined AI with rule-based checks**
   - AI output + rule-based checks.
   - If either flagged, content was reviewed.

6. **Manual review for edge cases**
   - Low-confidence cases went to human moderators.
   - This data was used to improve the system."

**Follow-up: How did you set the confidence threshold?**

"We experimented. Initially, we set it at 0.7. But we saw too many false positives. We increased it to 0.85 and saw better results. For critical categories like hate speech, we set a lower threshold to be safe.

The threshold is a trade-off between precision and recall."

**Follow-up: What if the model failed completely?**

"We had a fallback:
1. If model failed, we used rule-based checks.
2. If rule-based also failed, we marked it for manual review.
3. The user's content wasn't blocked — it was held for review.

This ensured the system never broke completely."

---

**Q90. What is hallucination in LLM?**

"Hallucination happens when an LLM generates information that sounds correct but is actually incorrect. The model 'hallucinates' facts.

**Examples:**
- Making up quotes from real people.
- Inventing historical events.
- Providing wrong medical advice.
- Citing non-existent papers.

**Why it happens:**
LLMs are trained to predict the next word. They don't have a fact-checking mechanism. They generate what's statistically likely, not what's true.

**How we reduced it in moderation:**

1. **Clear instructions** — prompts were specific and unambiguous.
2. **Limited scope** — model only did classification, not generation.
3. **Validation** — we validated outputs against expected categories.
4. **Rule-based checks** — combined with AI to catch errors.
5. **Manual review** — low-confidence cases went to humans.

**In my moderation project, hallucination was less of an issue because we used BERT-based classification, not generation. But it's a critical concern for LLM-based applications."**

**Follow-up: How do you detect hallucination?**

"1. **Cross-reference** — check facts against trusted sources.
2. **Consistency checks** — ask the same question multiple times.
3. **Confidence scores** — lower confidence may indicate hallucination.
4. **Human review** — for critical applications.
5. **RAG** — ground the model with retrieved facts."

**Follow-up: Can hallucination be fully eliminated?**

"No. It's a fundamental limitation of current LLMs. But it can be reduced through:
- Better prompts
- RAG
- Fine-tuning
- Human-in-the-loop
- Validation layers"

---

# PART 2: HUGGING FACE & NLP (Q91–Q95)

---

**Q91. What are embeddings?**

"Embeddings are numerical representations of text or data. They convert words or sentences into vectors where similar meanings have similar vector positions.

**Example:**
```
'king'  → [0.2, 0.5, 0.1, ...]
'queen' → [0.3, 0.6, 0.1, ...]
'apple' → [0.8, 0.1, 0.9, ...]
```

'king' and 'queen' are close in vector space. 'apple' is far.

**Use cases:**
1. **Semantic search** — find similar documents.
2. **Recommendation systems** — find similar items.
3. **Clustering** — group similar texts.
4. **RAG** — retrieve relevant context for LLMs.
5. **Classification** — features for ML models.

**In my work:**
I've used embeddings for content similarity. If two pieces of content had similar embeddings, they might be duplicates or related."

**Follow-up: What is cosine similarity?**

"Cosine similarity measures the angle between two vectors. It's used to find how similar two embeddings are.

```
cosine_similarity(A, B) = (A · B) / (||A|| * ||B||)
```

Range: -1 to 1. 1 means identical, 0 means no similarity, -1 means opposite."

**Follow-up: What is the difference between word embeddings and sentence embeddings?**

"**Word embeddings** — one vector per word. Doesn't capture context.
**Sentence embeddings** — one vector per sentence. Captures context.

For example, 'bank' in 'river bank' and 'bank account' would have different sentence embeddings but the same word embedding."

---

**Q92. Explain RAG.**

"RAG stands for Retrieval Augmented Generation. Instead of depending only on the model's internal knowledge, RAG retrieves relevant information from external sources and provides that context to the LLM.

**Why RAG?**
1. **LLMs have knowledge cutoff** — they don't know recent events.
2. **LLMs hallucinate** — they make up facts.
3. **LLMs don't know your data** — they weren't trained on your documents.

**How RAG works:**

```
User Query
    ↓
Embedding
    ↓
Vector Database Search
    ↓
Relevant Documents
    ↓
LLM generates response using retrieved context
```

**Components:**
1. **Document store** — your knowledge base.
2. **Embedding model** — converts text to vectors.
3. **Vector database** — stores and searches embeddings.
4. **LLM** — generates response.

**In my work:**
I haven't implemented RAG in production, but I understand the concept. For moderation, we could have used RAG to retrieve similar past cases and use them as context."

**Follow-up: What is a vector database?**

"A vector database stores embeddings and allows similarity search. Examples:
- Pinecone
- Weaviate
- Milvus
- Chroma
- FAISS (Facebook AI Similarity Search)

They're optimized for fast nearest-neighbor search in high-dimensional space."

**Follow-up: RAG vs Fine-tuning?**

"**RAG** — retrieves external knowledge. Good for dynamic data.
**Fine-tuning** — modifies model weights. Good for style, format, domain adaptation.

RAG is cheaper and faster to update. Fine-tuning is better for deep domain knowledge."

---

**Q93. What is Hugging Face?**

"Hugging Face is an open-source platform that provides pretrained machine learning models, datasets, and tools mainly for NLP and AI applications.

**What they offer:**
1. **Transformers library** — pretrained models for NLP.
2. **Datasets library** — thousands of datasets.
3. **Model Hub** — community-shared models.
4. **Spaces** — hosted ML apps.
5. **Inference API** — hosted model inference.

**In my work:**
I used Hugging Face Transformers for NLP-based content analysis and toxicity detection. The library made it easy to:
- Load pretrained models
- Tokenize text
- Run inference
- Post-process results

**Example:**
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased")
result = classifier("This is a great product!")
```

**Follow-up: What models have you used?**

"Mainly DistilBERT for text classification. I've also explored:
- BERT for understanding tasks
- RoBERTa for better accuracy
- Sentence-transformers for embeddings"

**Follow-up: Is Hugging Face free?**

"The library is free and open-source. Models are free to use. But:
- Some models have licenses (for commercial use).
- Inference API has free tier and paid tiers.
- Enterprise features are paid.

For our use case, we used open-source models, so no cost."

---

**Q94. Which Hugging Face model did you use?**

"For NLP-based moderation, we worked with transformer-based models. The main model was DistilBERT for toxicity detection and text classification.

**Why DistilBERT?**
1. **Speed** — 60% faster than BERT.
2. **Size** — 40% smaller.
3. **Accuracy** — retains 97% of BERT's performance.
4. **Cost** — cheaper to run in production.

**Specific model:**
We used `distilbert-base-uncased` for general text classification, and fine-tuned variants for specific toxicity categories.

**Pipeline:**
1. Text input from user.
2. Tokenization using DistilBERT tokenizer.
3. Model inference.
4. Post-processing to map output to categories.
5. Confidence threshold check.
6. Store result in database."

**Follow-up: Did you consider other models?**

"Yes, we evaluated:
- **BERT** — better accuracy but slower.
- **RoBERTa** — better accuracy but larger.
- **ALBERT** — smaller but less accurate.
- **DistilBERT** — best trade-off for us.

We chose DistilBERT because real-time moderation needed speed."

**Follow-up: How did you handle model updates?**

"We versioned our models. When a new model was available, we:
1. Tested it on a validation set.
2. Compared metrics with the current model.
3. If better, deployed it.
4. Kept the old model for rollback.

We also A/B tested models in production."

---

**Q95. How do you evaluate a classification model?**

"For classification problems, we look at:

1. **Accuracy** — overall correctness. (TP + TN) / Total
2. **Precision** — of all positive predictions, how many were correct? TP / (TP + FP)
3. **Recall** — of all actual positives, how many did we catch? TP / (TP + FN)
4. **F1-Score** — harmonic mean of precision and recall. 2 * (P * R) / (P + R)
5. **Confusion Matrix** — table of TP, TN, FP, FN

**For moderation systems:**
- **Precision** is important — we don't want to wrongly flag safe content.
- **Recall** is important — we don't want to miss harmful content.
- **F1-Score** balances both.

**Example:**
```
              Predicted Positive  Predicted Negative
Actual Positive       TP                  FN
Actual Negative       FP                  TN
```

**In our moderation project:**
We monitored precision and recall weekly. If recall dropped, we lowered the confidence threshold. If precision dropped, we raised it.

**Follow-up: What is the trade-off between precision and recall?**

"There's always a trade-off. If you want high recall (catch all harmful content), you'll have lower precision (more false positives). If you want high precision (no false positives), you'll have lower recall (miss some harmful content).

For moderation, we usually prefer high recall — it's better to flag safe content for review than to miss harmful content."

**Follow-up: What is AUC-ROC?**

"AUC-ROC is a metric for binary classification. It measures the model's ability to distinguish between classes.

- AUC = 0.5 → random
- AUC = 1.0 → perfect

It's useful when classes are imbalanced."

---

# PART 3: CELERY & REDIS (Q96–Q98)

---

**Q96. Explain Celery architecture.**

"Celery follows a producer-consumer architecture. Let me explain with our use case.

**Components:**

1. **Producer** — Django API. Creates tasks.
2. **Message Broker** — Redis. Stores tasks in queue.
3. **Worker** — Celery worker. Consumes tasks and executes them.
4. **Result Backend** — Redis or database. Stores task results.

**Flow:**
```
Django API → Redis Queue → Celery Worker → Task Execution
                ↓
         Result Backend
```

**In our moderation project:**
1. User submits content.
2. Django API validates and stores initial record.
3. API creates a Celery task and pushes to Redis.
4. API returns immediately (doesn't wait for moderation).
5. Celery worker picks up the task.
6. Worker calls Hugging Face model.
7. Worker stores result in MySQL.
8. Admin dashboard shows moderation status.

**Benefits:**
1. **Responsive API** — user doesn't wait.
2. **Scalable** — add more workers.
3. **Reliable** — tasks are persisted in Redis.
4. **Retryable** — failed tasks can be retried."

**Follow-up: What is the difference between Celery and cron?**

"**Cron** — schedules tasks at fixed times. No queue, no retry, no distribution.
**Celery** — distributed task queue. Supports retries, scheduling, multiple workers.

Celery is for asynchronous tasks. Cron is for scheduled tasks. You can use Celery Beat for scheduling."

**Follow-up: How do you monitor Celery?**

"1. **Flower** — web-based monitoring tool.
2. **Logging** — log task start, success, failure.
3. **Sentry** — error tracking.
4. **Database** — store task status.
5. **Prometheus + Grafana** — metrics.

I've used Flower for development and logging + Sentry for production."

---

**Q97. Why Redis with Celery?**

"Redis is lightweight and very fast because it stores data in memory. In our project, it was used as a message broker between Django and Celery workers.

**Why Redis?**
1. **Speed** — in-memory, microsecond latency.
2. **Simplicity** — easy to set up and use.
3. **Reliability** — supports persistence.
4. **Pub/Sub** — supports publish-subscribe patterns.
5. **Community** — well-documented, widely used.

**Alternatives:**
- **RabbitMQ** — more features, more complex.
- **Amazon SQS** — managed, but vendor lock-in.
- **Kafka** — for high-throughput streaming.

For our use case, Redis was the right choice — simple, fast, and sufficient."

**Follow-up: What is the difference between Redis and RabbitMQ?**

"**Redis** — in-memory data store. Can be used as broker. Simpler. Faster.
**RabbitMQ** — dedicated message broker. More features (routing, priorities). More complex.

Redis is good for simple task queues. RabbitMQ is good for complex routing and enterprise messaging."

**Follow-up: What if Redis goes down?**

"Tasks in the queue would be lost unless Redis persistence is enabled. We enabled Redis persistence (RDB + AOF) to minimize data loss. Also, we had monitoring and alerts for Redis downtime."

---

**Q98. How do you handle failed Celery tasks?**

"We handle failures using a multi-layered approach:

1. **Exception handling**
   - Wrap task logic in try/except.
   - Log the error with context.

2. **Retry mechanism**
   - Use `@task(bind=True, max_retries=3)`.
   - Retry on transient failures (network, timeout).
   - Exponential backoff.

3. **Logging**
   - Log task ID, input, error, and retry count.
   - Use structured logging for easy search.

4. **Monitoring**
   - Flower for real-time monitoring.
   - Alerts for failed tasks.

5. **Dead letter queue**
   - After max retries, move task to dead letter queue.
   - Manual review and reprocessing.

6. **Fallback logic**
   - If AI model fails, use rule-based checks.
   - If rule-based fails, mark for manual review.

**Example:**
```python
@shared_task(bind=True, max_retries=3)
def moderate_content(self, content_id):
    try:
        content = Content.objects.get(id=content_id)
        result = run_nlp_model(content.text)
        content.moderation_result = result
        content.save()
    except Exception as e:
        logger.error(f"Moderation failed for {content_id}: {e}")
        if self.request.retries < self.max_retries:
            raise self.retry(exc=e, countdown=60)
        else:
            content.status = 'manual_review'
            content.save()
```

**Follow-up: What is exponential backoff?**

"Exponential backoff means increasing the wait time between retries. For example:
- 1st retry: 60 seconds
- 2nd retry: 120 seconds
- 3rd retry: 240 seconds

This prevents overwhelming the system with retries."

**Follow-up: How do you handle idempotency?**

"Idempotency means running the same task multiple times has the same effect. We ensure this by:
1. Checking if task already completed.
2. Using unique task IDs.
3. Making operations idempotent — like upsert instead of insert."

---

# PART 4: AWS (Q99–Q100)

---

**Q99. Explain your AWS experience.**

"I have experience using AWS mainly with EC2 and S3.

**EC2 (Elastic Compute Cloud):**
- Used for hosting backend applications.
- Configured Linux environment.
- Deployed Django applications with Gunicorn and Nginx.
- Managed security groups and key pairs.

**S3 (Simple Storage Service):**
- Used for storing files and static assets.
- Configured bucket policies and permissions.
- Used presigned URLs for secure uploads.
- Integrated with Django using `django-storages`.

**Other services I've worked with:**
- **RDS** — managed databases (MySQL, PostgreSQL).
- **ElastiCache** — managed Redis.
- **CloudWatch** — monitoring and logging.
- **IAM** — access management.
- **Route 53** — DNS management.

**In my moderation project:**
We used EC2 for the Django application, RDS for MySQL, ElastiCache for Redis, and S3 for storing user-uploaded content."

**Follow-up: What is the difference between EC2 and Lambda?**

"**EC2** — virtual servers. You manage the OS. Good for long-running applications.
**Lambda** — serverless. You just deploy code. Good for event-driven, short tasks.

EC2 is better for our use case because we had a Django application that needed to run continuously."

**Follow-up: What is the difference between S3 and EBS?**

"**S3** — object storage. Good for files, backups, static assets.
**EBS** — block storage. Good for databases, EC2 volumes.

S3 is accessed via HTTP. EBS is accessed as a disk."

---

**Q100. How would you deploy a Django AI application on AWS?**

"This is a comprehensive deployment question. Let me explain step by step.

**Architecture:**
```
Client
    ↓
Route 53 (DNS)
    ↓
CloudFront (CDN)
    ↓
Application Load Balancer
    ↓
EC2 (Nginx + Gunicorn + Django)
    ↓
RDS (MySQL) + ElastiCache (Redis) + S3 (Files)
    ↓
Celery Workers (EC2)
    ↓
Hugging Face Model (on workers)
```

**Step-by-step deployment:**

1. **Create EC2 instance**
   - Choose Ubuntu.
   - Configure security groups.
   - Set up SSH access.

2. **Configure Linux environment**
   - Update packages.
   - Install Python, pip, virtualenv.
   - Install Nginx, Gunicorn.

3. **Deploy Django application**
   - Clone repository.
   - Create virtual environment.
   - Install dependencies.
   - Configure environment variables.

4. **Run Django with Gunicorn**
   - Create systemd service.
   - Configure workers.
   - Start Gunicorn.

5. **Configure Nginx**
   - Reverse proxy to Gunicorn.
   - Serve static files.
   - SSL termination.

6. **Setup database**
   - Create RDS instance.
   - Configure security groups.
   - Run migrations.

7. **Configure Redis**
   - Create ElastiCache cluster.
   - Configure Celery.

8. **Run Celery workers**
   - Create systemd service.
   - Configure concurrency.
   - Start workers.

9. **Store files on S3**
   - Create S3 bucket.
   - Configure `django-storages`.
   - Set up IAM roles.

10. **Enable monitoring and logging**
    - CloudWatch for logs.
    - CloudWatch alarms.
    - Sentry for error tracking.

11. **Set up CI/CD**
    - GitHub Actions or AWS CodePipeline.
    - Automated testing.
    - Automated deployment.

12. **Configure auto-scaling**
    - Auto Scaling Group for EC2.
    - Load balancer for distribution.
    - Scale based on CPU or requests.

**Follow-up: How do you handle model deployment?**

"The Hugging Face model is loaded on Celery workers. When a worker starts, it loads the model into memory. This takes time, so we keep workers warm. For updates, we use a rolling deployment — new workers load the new model, then old workers are terminated."

**Follow-up: How do you handle model inference cost?**

"Model inference can be expensive. We optimized by:
1. **Batching** — process multiple requests together.
2. **Caching** — cache frequent predictions.
3. **Smaller models** — DistilBERT instead of BERT.
4. **Spot instances** — for non-critical workers.
5. **Auto-scaling** — scale down when traffic is low."

**Follow-up: How do you secure the deployment?**

"1. **VPC** — isolate resources.
2. **Security groups** — restrict access.
3. **IAM roles** — least privilege.
4. **SSL/TLS** — encrypt traffic.
5. **Secrets Manager** — store secrets.
6. **WAF** — protect against attacks.
7. **Regular updates** — patch vulnerabilities."

---

# PART 5: QUICK REVISION CHECKLIST (Module 5)

---

## AI Moderation Project

- [ ] Project overview — problem, solution, architecture
- [ ] My role — backend development, Hugging Face integration
- [ ] Challenges — accuracy vs speed, false positives
- [ ] Why Hugging Face — pretrained vs custom
- [ ] Did you train the model? — No, used pretrained
- [ ] Fine-tuning vs pretrained

## LLM & NLP

- [ ] LLM — definition, examples, limitations
- [ ] Transformer architecture — encoder, decoder, attention
- [ ] Self-attention — how it works
- [ ] Multi-head attention
- [ ] BERT vs GPT — encoder vs decoder
- [ ] Encoder-only vs Decoder-only vs Encoder-Decoder
- [ ] DistilBERT — knowledge distillation, why used
- [ ] Inconsistent model responses — handling strategy
- [ ] Hallucination — cause, prevention
- [ ] Embeddings — vectors, use cases
- [ ] Cosine similarity
- [ ] RAG — retrieval augmented generation
- [ ] Vector databases
- [ ] Hugging Face — platform, Transformers library
- [ ] Model evaluation — accuracy, precision, recall, F1
- [ ] Confusion matrix
- [ ] AUC-ROC

## Celery & Redis

- [ ] Celery architecture — producer, broker, worker
- [ ] Why Redis with Celery
- [ ] Redis vs RabbitMQ
- [ ] Failed task handling — retry, logging, dead letter queue
- [ ] Exponential backoff
- [ ] Idempotency

## AWS

- [ ] EC2 — virtual servers
- [ ] S3 — object storage
- [ ] RDS — managed databases
- [ ] ElastiCache — managed Redis
- [ ] CloudWatch — monitoring
- [ ] IAM — access management
- [ ] Django AI deployment — step by step
- [ ] Model deployment — workers, rolling updates
- [ ] Cost optimization
- [ ] Security best practices

---

# PART 6: INTERVIEW TIPS (Google, Microsoft, Amazon)

---

1. **Be honest about what you did** — "I used pretrained models, I didn't train them from scratch" is a strong answer, not a weak one.

2. **Explain the architecture** — draw diagrams. Show the flow from user request to moderation result.

3. **Talk about trade-offs** — DistilBERT vs BERT, RAG vs fine-tuning, Redis vs RabbitMQ.

4. **Mention production challenges** — handling failures, retries, monitoring, scaling.

5. **Connect to your project** — "In my moderation project, we used Celery because..."

6. **Show depth** — mention knowledge distillation, attention mechanism, confidence thresholds.

7. **Be realistic** — "We didn't have labeled data for fine-tuning, so we used pretrained models."

8. **Think about scale** — "For 1 million requests per day, we would need..."

---

**Practice Tip:** AI/ML questions mein interviewer depth check karega — especially "Did you train the model?" aur "How did you handle failures?" Ke answers clear rakho. Jo kiya hai wahi bolo, fake mat karo. Product companies value honesty and practical thinking over buzzwords.

---

[← Previous: Module 4](module-4-mysql-sql.md) | [Back to Index](README.md) | [Next: Module 6 →](module-6-system-design-coding.md)
