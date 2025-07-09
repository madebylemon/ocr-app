import os
import tempfile
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes

app = FastAPI()

# Allow frontend dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract")
async def extract_text(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        text = ""
        if file.content_type.startswith("image/"):
            # Reset file pointer and open image
            file.file.seek(0)
            image = Image.open(file.file)
            text = pytesseract.image_to_string(image, lang="vie+eng")
        elif file.content_type == "application/pdf":
            images = convert_from_bytes(contents)
            text = "\n".join([pytesseract.image_to_string(img, lang="vie+eng") for img in images])
        else:
            return JSONResponse({"error": "Unsupported file type."}, status_code=400)
        return {"text": text}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
