# RAG-chatbot-Gemini-API-ollama

# ---------------------------
# ✅ 1) Clone your repo
# ---------------------------
echo "📥 Cloning repo..."
git clone https://github.com/BhagyeshPatil2004/RAG-chatbot-Gemini-API-ollama.git
cd RAG-chatbot-Gemini-API-ollama

# ---------------------------
# ✅ 2) Create .env placeholder
# ---------------------------
echo "🔑 Creating .env..."
echo 'GEMINI_API_KEY="YOUR_GEMINI_API_KEY"' > .env

# ---------------------------
# ✅ 3) Create .gitignore
# ---------------------------
echo "🗂️  Creating .gitignore..."
cat <<EOL > .gitignore
# Python
__pycache__/
*.pyc
.venv/

# Env
.env

# VSCode
.vscode/

# Chroma DB
chroma_db/
EOL

# ---------------------------
# ✅ 4) Write README.md
# ---------------------------
echo "📝 Writing README.md..."
cat <<EOL > README.md
# RAG-chatbot-Gemini-API-ollama 🤖

This is a simple Retrieval-Augmented Generation (RAG) chatbot built using:
- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://github.com/ollama/ollama)
- [ChromaDB](https://www.trychroma.com/)

It uses the **original codebasics FAQ dataset** from [this video](https://www.youtube.com/watch?v=AjQPRomyd-k).  
**Note:** I did **some changes in the code only — the dataset remains the same.**

---

## ⚙️ Features

✅ Loads CSV data of FAQs  
✅ Creates embeddings with Ollama (\`mxbai-embed-large\`)  
✅ Stores embeddings locally in ChromaDB  
✅ Uses Gemini API (or your local LLM) to generate answers  
✅ Runs a simple CLI chat loop

---

## 📚 Dataset

- \`codebasics_faqs.csv\` is sourced from the [codebasics YouTube channel](https://www.youtube.com/watch?v=AjQPRomyd-k)
- **No modifications to dataset** — only code improved to fit this RAG structure.

---

## 🚀 How to Run

### 1️⃣ Clone the Repo

\`\`\`bash
git clone https://github.com/BhagyeshPatil2004/RAG-chatbot-Gemini-API-ollama.git
cd RAG-chatbot-Gemini-API-ollama
\`\`\`

### 2️⃣ Setup Python Environment

\`\`\`bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
\`\`\`

### 3️⃣ Add your Gemini API key

Edit \`.env\` and replace with your real API key.

### 4️⃣ Make sure Ollama is running

\`\`\`bash
ollama pull mxbai-embed-large
\`\`\`

### 5️⃣ Run the chatbot

\`\`\`bash
python "AI Agent 1/agent.py"
\`\`\`

---

## ✅ Notes

- Ollama must be running for embeddings.
- Gemini API generates answers.
- Easily swap a bigger dataset for your major project.

---

## 👨‍💻 Author

**[Bhagyesh Patil](https://github.com/BhagyeshPatil2004)**  
📌 Repo: [RAG-chatbot-Gemini-API-ollama](https://github.com/BhagyeshPatil2004/RAG-chatbot-Gemini-API-ollama)

---
EOL

# ---------------------------
# ✅ 5) Create requirements.txt
# ---------------------------
echo "📦 Creating requirements.txt..."
cat <<EOL > requirements.txt
langchain
langchain_community
langchain_ollama
langchain_chroma
ollama
python-dotenv
EOL

# ---------------------------
# ✅ 6) Setup Python venv + install
# ---------------------------
echo "🐍 Creating Python venv..."
python -m venv .venv

echo "🐍 Activating venv & installing..."
# Detect OS to activate venv properly
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    .venv\\Scripts\\activate && pip install -r requirements.txt
else
    source .venv/bin/activate && pip install -r requirements.txt
fi

# ---------------------------
# ✅ 7) Pull Ollama embedding model
# ---------------------------
echo "🧠 Pulling Ollama embedding model..."
ollama pull mxbai-embed-large

# ---------------------------
# ✅ Done!
# ---------------------------
echo ""
echo "1️⃣  Add your real Gemini API key in .env"
echo "2️⃣  Make sure Ollama is running"
echo "3️⃣  Run your bot: python \"AI Agent 1/agent.py\""
echo ""
echo "🔥 Happy!"
