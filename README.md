# 🏥 Medical OCR Document Extraction API

This project is a **FastAPI-based OCR system** that extracts structured information from unstructured medical documents like prescriptions and patient detail forms. It uses **Tesseract OCR** and **OpenCV** to process PDFs, extract text from images, and return structured data via a RESTful API.

---

## 🚀 Features

- 🔍 OCR-based text extraction from medical PDFs (prescriptions & patient details)
- 🧠 Custom parsers for structured detail extraction (`PatientParser`, `PrescriptionParser`)
- ⚙️ API endpoints built with FastAPI to handle file uploads and return JSON data
- 🔁 Test-Driven Development (TDD): test cases written for every detail extraction
- 🧪 Integrated testing ensures reliability and correctness of extraction logic
- 🧰 Postman used for manual API testing

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **OpenCV**
- **Tesseract OCR**
- **PyPDF2 / pdf2image** (for PDF-to-image conversion)
- **Pytest** (for TDD)
- **Postman** (for API testing)

---


