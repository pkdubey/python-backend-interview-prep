# 📧 SETUP EMAIL — Send This 3 Days Before Day 1

**Subject:** Python AI Training — Please Install These Before Day 1 (Takes 20 mins)

---

Hi Team,

Excited to see you all on **17th November** for our 15-day Python AI Training!

Before Day 1, please spend **20 minutes** installing the tools below.  
This saves us from wasting the first hour fixing setup issues in class.

---

## Step 1: Install Python 3.11

👉 https://www.python.org/downloads/release/python-3110/

- Download the installer for your OS
- **Windows users:** Check ✅ "Add Python to PATH" during install
- Verify: Open terminal and type `python --version` → should show `3.11.x`

---

## Step 2: Install VS Code

👉 https://code.visualstudio.com/

- Install the **Python extension** inside VS Code (search "Python" in Extensions tab)
- Install the **Jupyter extension** too

---

## Step 3: Install Ollama (for running AI locally — FREE, no API key needed)

👉 https://ollama.com/download

- Download and install for your OS
- Open terminal and run: `ollama pull llama3.2`
- This downloads a ~2GB AI model. Do this on good WiFi.
- Verify: `ollama run llama3.2` → type "hello" → it should respond

---

## Step 4: Create a folder for the training

```bash
mkdir ai-training
cd ai-training
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
pip install jupyter notebook pandas numpy matplotlib
```

---

## Step 5 (Optional): OpenAI API Key

If you have access to an OpenAI account:
- Go to https://platform.openai.com/api-keys
- Create a key and save it somewhere safe
- We'll use this from Day 6 onwards (Ollama is the free alternative)

---

## ❓ Stuck?

Reply to this email or WhatsApp me. Don't worry if something doesn't work — we'll sort it out together on Day 1 morning.

See you soon! 🚀

**Pavan Kumar Dubey**  
Python AI Trainer | 5.5+ Years Experience
