# OCR Extract Pro

A full-stack application for extracting text from images and PDF documents using OCR (Optical Character Recognition).

## Features
- Upload images (JPG, PNG, GIF, WebP) and PDF files
- Real-time OCR extraction using a FastAPI backend and Tesseract
- Modern React frontend with drag-and-drop, batch processing, and beautiful UI
- Download or copy extracted text

---

## Project Structure
```
ocr-extract/
├── backend/           # FastAPI OCR backend
│   ├── main.py
│   └── requirements.txt
└── frontend/          # React frontend
    ├── src/
    ├── public/
    ├── package.json
    └── ...
```

---

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- Tesseract OCR installed on your system ([installation guide](https://github.com/tesseract-ocr/tesseract))

### 1. Backend Setup
```sh
cd backend
pip install -r requirements.txt
# Start the FastAPI server
python3 -m uvicorn main:app --reload
```
- The API will be available at `http://127.0.0.1:8000/extract`

### 2. Frontend Setup
```sh
cd frontend
npm install
npm start
```
- The app will open at `http://localhost:3000`

---

## Usage
1. Start both backend and frontend servers.
2. Upload images or PDFs in the web UI.
3. Click "Process" to extract text using OCR.
4. Download or copy the extracted text.

---

## Deployment
- You can deploy the backend (FastAPI) to any Python-friendly host (e.g., Heroku, Render, AWS, etc.).
- The frontend can be deployed to Vercel, Netlify, or any static hosting.
- Update the API endpoint in the frontend if deploying separately.

---

## Credits
- [React](https://react.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Tailwind CSS](https://tailwindcss.com/)
- [Lucide Icons](https://lucide.dev/)

---

## License
MIT
