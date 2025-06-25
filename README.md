# Assignment AIPlanet

This repository contains a full-stack application for PDF Question & Answering using Google Gemini (Generative AI). The project consists of a FastAPI backend and a React frontend.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features

- Upload PDF documents.
- Ask questions about the uploaded PDF using Google Gemini LLM.
- Vector store caching for efficient retrieval.
- Modern React-based UI.

---

## Project Structure
assignmentAIPlanet/ 
├── backend/ 
│   ├── app/ 
│   │ ├── main.py
│   │ └── checModel.py 
│   ├── uploads/ 
│   ├── vector_store/ 
│   ├── requirements.txt 
│   ├── .env.example 
│   └── README.md 
├── frontend/ 
│   ├── src/ 
│   │ ├── App.jsx 
│   │ ├── App.css 
│   │ ├── main.jsx 
│   │ └── components/ 
│   │ ├── FileUploads.jsx 
│   │ └── ChatInterface.jsx 
│   ├── public/ 
│   ├── package.json 
│   ├── vite.config.js 
│   └── README.md 
└── README.md

---

## Prerequisites

- **Python 3.8+**
- **Node.js v16+** and **npm** or **yarn**
- **Google Generative AI API Key** (see [Environment Variables](#environment-variables))

---

## Setup Instructions

### Backend Setup

1. **Navigate to the backend folder:**
    ```bash
    cd backend
    ```

2. **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure environment variables:**
    - Copy `.env.example` to `.env` and add your Google API key:
      ```
      GOOGLE_API_KEY=your_google_api_key_here
      ```

4. **Run the backend server:**
    ```bash
    uvicorn app.main:app --reload
    ```
    - The backend will be available at [http://localhost:8000](http://localhost:8000).

### Frontend Setup

1. **Navigate to the frontend folder:**
    ```bash
    cd frontend
    ```

2. **Install Node dependencies:**
    ```bash
    npm install
    # or
    yarn install
    ```

3. **Start the frontend development server:**
    ```bash
    npm run dev
    # or
    yarn dev
    ```
    - The frontend will be available at [http://localhost:5173](http://localhost:5173) (default Vite port).

---

## Usage

1. Open the frontend in your browser.
2. Upload a PDF document.
3. Ask questions about the uploaded PDF in the chat interface.

---

## Environment Variables

### Backend

- [.env](http://_vscodecontentref_/14) file in the [backend](http://_vscodecontentref_/15) directory:
    ```
    GOOGLE_API_KEY=your_google_api_key_here
    ```

### Frontend

- No environment variables are required by default. If you want to change the backend API URL, update the endpoints in the frontend source code.

---

## API Endpoints

- **POST `/upload`**  
  Upload a PDF file.  
  **Body:** `multipart/form-data` with a `file` field.

- **POST `/ask`**  
  Ask a question about an uploaded PDF.  
  **Body:**  
  ```json
  {
    "filename": "your_uploaded_file.pdf",
    "question": "Your question here"
  }
  ```

