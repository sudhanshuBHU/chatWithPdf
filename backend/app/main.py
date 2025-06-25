import os
import shutil
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# --- NEW IMPORTS for Google Gemini ---
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

# --- Load API Key from .env ---
load_dotenv()
if os.getenv("GOOGLE_API_KEY") is None:
    raise Exception("GOOGLE_API_KEY not found in .env file")

# --- FastAPI App Initialization ---
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Global Variables & Constants ---
UPLOADS_DIR = "uploads"
VECTOR_STORE_DIR = "vector_store"
os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(VECTOR_STORE_DIR, exist_ok=True)


# --- Pydantic Models ---
class QuestionRequest(BaseModel):
    filename: str
    question: str


# --- Helper Function for QA Chain (MODIFIED for Google Gemini) ---
def get_qa_chain(file_path: str):
    file_name = os.path.basename(file_path)
    vector_store_path = os.path.join(VECTOR_STORE_DIR, f"{file_name}.faiss.google")

    # 1. Initialize Google Embeddings
    # This model is specifically for creating embeddings for text.
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    if os.path.exists(vector_store_path):
        print(f"Loading existing Google vector store for {file_name}")
        vector_store = FAISS.load_local(vector_store_path, embeddings, allow_dangerous_deserialization=True)
    else:
        print(f"Creating new Google vector store for {file_name}")
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        texts = text_splitter.split_documents(documents)
        vector_store = FAISS.from_documents(texts, embeddings)
        vector_store.save_local(vector_store_path)
    
    # 2. Initialize the Gemini LLM
    # This is the model that will answer the questions.
    llm = GoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        return_source_documents=False,
    )
    return qa_chain


# --- API Endpoints ---

@app.get("/")
async def root():
    return {"message": "Welcome to the PDF Question Answering API using Google Gemini!"}

@app.post("/upload")
# ... (The /upload endpoint code is exactly the same as before)
async def upload_file(file: UploadFile = File(...)):
    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDFs are allowed.")

    file_path = os.path.join(UPLOADS_DIR, file.filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {e}")
    finally:
        file.file.close()
    
    return {"filename": file.filename, "detail": "File uploaded successfully"}


@app.post("/ask")
# ... (The /ask endpoint code is exactly the same, using the updated invoke method)
async def ask_question(request: QuestionRequest):
    file_path = os.path.join(UPLOADS_DIR, request.filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found. Please upload the file first.")

    try:
        print(f"Processing question for {request.filename} using Google Gemini: '{request.question}'")
        qa_chain = get_qa_chain(file_path)
        answer = qa_chain.invoke({"query": request.question})
        return {"answer": answer['result']}
    except Exception as e:
        print(f"Error during QA processing: {e}")
        # A specific error can happen if content is blocked by Google's safety settings
        if "response was blocked by the safety " in str(e):
             return {"answer": "The response was blocked by Google's safety filters. Please try rephrasing your question."}
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")