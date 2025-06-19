from langchain_google_genai import GoogleGenerativeAI
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from langchain_community.document_loaders import CSVLoader
from langchain.chains import RetrievalQA
import os 
from dotenv import load_dotenv

load_dotenv()

# 1. Load Gemini model
llm = GoogleGenerativeAI(
    model = "gemini-1.5-flash",
    google_api_key = os.getenv("GEMINI_API")
)


# 2. Use Ollama for embeddings
embedding = OllamaEmbeddings(model="mxbai-embed-large")

# 3. Load and embed documents (CSV/URLs etc.)
loader = CSVLoader(file_path=r"C:\AI Agent demo\AI Agent 1\codebasics_faqs.csv", source_column="prompt")
docs = loader.load()


# 4. Store embeddings in ChromaDB
db = Chroma.from_documents(
    documents=docs,
    embedding=embedding,
    persist_directory="./chroma_db"
)

retriever =db.as_retriever()

# 5. RAG Prompt
prompt = ChatPromptTemplate.from_template("""
You are an expert assistant.
Use the following context to answer the question.
If unsure, say "I don't know".

Context:
{context}

Question:
{question}
""")

# 6. Chain
chain = prompt | llm

# 7. RAG loop (basic)
while True:
    query = input("Ask your question (q to quit): ")
    if query.lower() == "q":
        break
    
    context_docs = retriever.invoke(query)
    context ="n\n".join([doc.page_content for doc in context_docs])
    result = chain.invoke({"context": context, "question": query})

    print("\n Answer", result)