# Module 5: LLM, Hugging Face, Celery, Redis, AWS (Q81–Q100)

[← Back to Index](README.md) | [← Previous: Module 4](module-4-mysql-sql.md)

---

**Q81. Explain your AI-based content moderation project.**

"The project was an AI-powered content moderation system for user-generated content on the Neighborshook platform. The main objective was to automatically identify harmful content like toxicity, spam, harassment, or policy violations.

The backend was built using Laravel and Django REST APIs. When a user submitted content, the request was validated and processed. For AI analysis, we integrated Hugging Face Transformers — mainly DistilBERT — for NLP-based toxicity detection and text classification.

The moderation result was stored in MySQL and exposed through APIs for the admin moderation dashboard. The system also had rule-based checks along with AI-based classification to improve reliability."

**Follow-up: What was your exact contribution?**

"My main contribution was backend development. I worked on Django/Laravel APIs, Hugging Face integration, NLP pipeline, database handling, error handling, and moderation dashboard APIs."

---

**Q82. Why did you use Hugging Face instead of building your own model?**

"Training a transformer model from scratch requires huge datasets, computational resources, and infrastructure. Our requirement was mainly text classification for toxicity detection, so using pretrained models from Hugging Face allowed us to integrate advanced NLP faster. We focused on model selection, integration, response handling, and application-level workflow."

---

**Q83. What is an LLM?**

"LLM stands for Large Language Model. It is a deep learning model trained on a huge amount of text data to understand and generate human-like language. It can perform tasks like text classification, summarization, question answering, translation, and content generation."

**Follow-up: Examples of LLMs?**

"GPT models, Gemini, Claude, Llama, and Mistral are examples of LLMs."

---

**Q84. Explain Transformer architecture.**

"Transformer is a deep learning architecture introduced for natural language processing. The main concept is attention mechanism, which allows the model to understand relationships between words regardless of their position. Unlike RNNs, transformers process sequences in parallel, which makes training faster and allows handling longer contexts."

---

**Q85. What is Self-Attention?**

"Self-attention allows a model to understand which words are important in relation to other words in the same sentence. For example, in a sentence, the model can understand which words are related and assign different importance scores."

**Follow-up: Why is attention important?**

"Because language depends on context. Attention helps the model capture long-range relationships between words."

---

**Q86. Difference between BERT and GPT?**

"BERT is mainly an encoder-based model. It understands context from both directions and is commonly used for tasks like classification and sentiment analysis. GPT is decoder-based and mainly designed for text generation. BERT is good for understanding text, while GPT is good for generating text."

---

**Q87. Difference between Encoder-only and Decoder-only models?**

"Encoder-only models like BERT are mainly used for understanding tasks such as classification and embeddings. Decoder-only models like GPT generate text by predicting the next token. Encoder-decoder models like T5 are used for tasks where input is converted into output, such as translation or summarization."

---

**Q88. What is DistilBERT and why did you use it?**

"DistilBERT is a smaller, faster, and lighter version of BERT. It retains most of BERT's language understanding while being more efficient for inference. For our moderation system, we needed fast classification of user-generated content, so DistilBERT was a good trade-off between accuracy and speed compared to full BERT."

---

**Q89. How did you handle inconsistent model responses?**

"NLP model responses can sometimes vary. To handle this:
- We defined strict classification categories.
- Used confidence thresholds.
- Added validation on the backend.
- Handled unexpected responses with exception handling.
- Combined AI output with rule-based checks.
- Marked low-confidence cases for manual review."

---

**Q90. What is hallucination in LLM?**

"Hallucination happens when an LLM generates information that sounds correct but is actually incorrect. For content moderation, we reduced this risk by giving clear instructions, limiting the task scope, validating responses, and combining AI output with rule-based checks."

---

**Q91. What are embeddings?**

"Embeddings are numerical representations of text or data. They convert words or sentences into vectors where similar meanings have similar vector positions. They are commonly used in semantic search, recommendation systems, and RAG applications."

---

**Q92. Explain RAG.**

"RAG stands for Retrieval Augmented Generation. Instead of depending only on the model's internal knowledge, RAG retrieves relevant information from external sources and provides that context to the LLM.

Flow:
User Query → Embedding → Vector Database Search → Relevant Documents → LLM generates response."

---

**Q93. What is Hugging Face?**

"Hugging Face is an open-source platform that provides pretrained machine learning models, datasets, and tools mainly for NLP and AI applications. I used Hugging Face Transformers for NLP-based content analysis and toxicity detection."

---

**Q94. Which Hugging Face model did you use?**

"For NLP-based moderation, we worked with transformer-based models. The main model was DistilBERT for toxicity detection and text classification. We chose it because it provides good performance with lower inference cost compared to full BERT."

**Follow-up: Why DistilBERT?**

"DistilBERT is smaller and faster than BERT while maintaining good language understanding, which makes it suitable for real-time classification use cases."

---

**Q95. How do you evaluate a classification model?**

"For classification problems, we look at:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

For moderation systems, precision and recall are important because false positives and false negatives both impact users."

---

**Q96. Explain Celery architecture.**

"Celery follows a producer-consumer architecture. In our case:
Django API acts as producer.
Redis works as message broker.
Celery workers consume tasks from Redis.
Workers execute the task and store the result."

```
Django → Redis Queue → Celery Worker → Task
```

---

**Q97. Why Redis with Celery?**

"Redis is lightweight and very fast because it stores data in memory. In our project, it was used as a message broker between Django and Celery workers. It helped manage background tasks efficiently."

---

**Q98. How do you handle failed Celery tasks?**

"We handle failures using:
- Exception handling
- Retry mechanism
- Logging
- Monitoring task status

For temporary failures like API timeout, we retry the task. For permanent failures, we log the issue and mark it for manual handling."

---

**Q99. Explain your AWS experience.**

"I have experience using AWS mainly with EC2 and S3. EC2 was used for hosting backend applications. S3 was used for storing files and static assets. For deployment, the typical setup is Django application running on EC2 behind Nginx and Gunicorn."

---

**Q100. How would you deploy a Django AI application on AWS?**

"A typical production deployment would be:
1. Create EC2 instance.
2. Configure Linux environment.
3. Install Python dependencies.
4. Run Django application using Gunicorn.
5. Configure Nginx as reverse proxy.
6. Setup database.
7. Configure Redis for Celery.
8. Run Celery workers.
9. Store files on S3.
10. Enable monitoring and logging."

---

## Quick Revision Checklist (Module 5)

- [ ] AI moderation project — complete flow
- [ ] Hugging Face vs custom model — why pretrained
- [ ] LLM — definition + examples
- [ ] Transformer architecture — attention mechanism
- [ ] Self-Attention — kya karta hai
- [ ] BERT vs GPT — encoder vs decoder
- [ ] Encoder-only vs Decoder-only vs Encoder-Decoder
- [ ] DistilBERT — why smaller + faster
- [ ] Inconsistent model responses — handling strategy
- [ ] Hallucination — cause + prevention
- [ ] Embeddings — vectors + use cases
- [ ] RAG — retrieval + generation flow
- [ ] Hugging Face — platform + Transformers
- [ ] Model evaluation — accuracy, precision, recall, F1
- [ ] Celery architecture — producer, broker, worker
- [ ] Redis as broker — why fast
- [ ] Celery task failures — retry + logging
- [ ] AWS — EC2, S3
- [ ] Django AI deployment — step-by-step

---

**Practice Tip:** AI/ML questions mein interviewer depth check karega — especially "Did you train the model?" aur "How did you handle failures?" Ke answers clear rakho. Jo kiya hai wahi bolo, fake mat karo.

---

[← Previous: Module 4](module-4-mysql-sql.md) | [Back to Index](README.md) | [Next: Module 6 →](module-6-system-design-coding.md)
