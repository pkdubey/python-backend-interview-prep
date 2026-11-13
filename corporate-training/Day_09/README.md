# Day 9 — Open Source LLMs
**Vibe:** "Cutting the cord from Big Tech — and why that matters for your company."

---

## 🗣️ How to Open This Day

> "Every time you call OpenAI's API, two things happen: you pay money, and your data leaves your company's servers. For a bank, a hospital, or a government project — that's a problem. Open source LLMs let you run AI on YOUR machine, with YOUR data, for FREE. Today we explore that world."

---

## 🧠 Concepts & Human-Language Explanations

### OpenAI vs Open Source — The Restaurant Analogy
**Say this:**
> "OpenAI is like ordering from a **5-star restaurant** — expensive, high quality, you don't know the recipe, and your order goes through their kitchen (their servers).
> 
> Open Source LLMs are like **buying ingredients and cooking yourself** — cheaper (or free), you control everything, it takes more effort, but your data never leaves your kitchen."

### Key Open Source Models

| Model | Made by | Best for |
|-------|---------|----------|
| Llama 3.2 | Meta | General purpose, great quality |
| Mistral 7B | Mistral AI | Fast, efficient, good for coding |
| Phi-3 | Microsoft | Tiny but smart, runs on laptops |
| Gemma 2 | Google | Balanced performance |
| CodeLlama | Meta | Code generation specifically |

### Model Sizes — "7B vs 70B"
**Say this:** "The number (7B, 13B, 70B) is the number of parameters — think of it as the model's 'brain cells'. More = smarter but slower and needs more RAM."

| Size | RAM needed | Speed | Quality |
|------|-----------|-------|---------|
| 3B | 4 GB | Very fast | Good for simple tasks |
| 7B | 8 GB | Fast | Good for most tasks |
| 13B | 16 GB | Medium | Better reasoning |
| 70B | 40+ GB | Slow | Near GPT-4 quality |

**Say this:** "For most corporate use cases, a 7B model is enough. It runs on a decent laptop."

### Quantization — "Compressing the Model"
**Say this:** "A 7B model in full precision needs 28 GB of RAM. Quantization compresses it — like a ZIP file for AI. A 4-bit quantized 7B model needs only 4-5 GB. Slight quality loss, but runs on your laptop."

**GGUF format** = The compressed format used by Ollama and LM Studio.

### HuggingFace — "The GitHub for AI Models"
**Say this:** "HuggingFace is where all open source AI models live. It's like GitHub but for AI. Over 500,000 models. You can download any of them for free."

Key things to show on HuggingFace website:
- Model cards (what the model does, how it was trained)
- Downloads per month (popularity indicator)
- License (MIT = free for commercial use, Llama license = need to check)
- Model size and requirements

---

## 💻 Live Coding Demo

**Demo 1:** Browse HuggingFace.co — show how to read a model card  
**Demo 2:** Use HuggingFace Inference API (free tier)  
**Demo 3:** Compare same prompt on Llama 3.2 vs Mistral via Ollama  

See `lab.py`.

---

## 🏋️ Hands-on Challenge

1. Go to HuggingFace.co and find a model for sentiment analysis
2. Use the HuggingFace Inference API to classify 5 reviews
3. Compare the results with TextBlob from Day 5
4. Discuss: Which is more accurate? Which is faster?

---

## 📝 Daily Recap Questions

1. "Name 2 reasons a company might prefer open source LLMs over OpenAI."
2. "What does '7B' mean in Llama 3.2 7B?"
3. "What is quantization and why does it matter?"

**Key takeaway:** "Open source AI is not 'worse' AI. For many tasks, a well-tuned 7B model beats GPT-3.5. And it's free, private, and you control it completely."
