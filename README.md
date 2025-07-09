
# OCR Extract Pro

An all-in-one OCR and invoice extraction suite for English and Vietnamese documents.


## Features

- **Image & PDF OCR**: Upload images (JPG, PNG, GIF, WebP) or PDF files for instant text extraction using Tesseract (supports English & Vietnamese).
- **Vietnamese Text Correction**: Automatically fix common OCR font/character errors in Vietnamese text, making the output more accurate and readable.
- **Invoice Data Extraction Suite**: Advanced tool for extracting structured invoice data (seller, buyer, invoice details, line items, payment info) from OCR text, supporting both English and Vietnamese field labels/values.
- **Export & Copy**: Download/copy extracted text, or export invoice data as JSON/CSV.
- **Modern UI**: Beautiful React frontend with drag-and-drop, batch upload, and responsive design (Tailwind CSS).
- **Backend**: FastAPI server with Tesseract OCR and PDF/image support.
- **Invoice Tool Access**: Click the app logo to open the Invoice Extraction Suite in a new tab.
- **Monorepo**: All code (frontend & backend) in a single repo for easy development and deployment.

---

## Vietnamese Text Correction

OCR on Vietnamese documents can sometimes produce incorrect or garbled characters due to font or encoding issues. This app includes a built-in tool that automatically detects and corrects common Vietnamese OCR errors, so your extracted text is more accurate and makes sense for further processing or export.

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
    │   └── invoice-extractor.html  # Standalone Invoice Extraction Suite
    ├── package.json
    └── ...
```

---

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- Tesseract OCR installed ([installation guide](https://github.com/tesseract-ocr/tesseract))

### 1. Backend Setup
```sh
cd backend
pip install -r requirements.txt
# Start the FastAPI server
uvicorn main:app --reload
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
2. Upload images or PDFs in the web UI for OCR extraction.
3. Click the app logo to open the Invoice Data Extraction Suite for advanced invoice field extraction (supports both English and Vietnamese labels/values).
4. Download/copy extracted text, or export invoice data as JSON/CSV.

---


## Deployment

- Deploy the backend (FastAPI) to any Python-friendly host (Heroku, Render, AWS, etc.).
- Deploy the frontend to Vercel, Netlify, or any static host.
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
