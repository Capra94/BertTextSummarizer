# Text Summarizer

## Overview

This project combines a Flask-based backend API and a React frontend to provide a user-friendly interface for text summarization. The backend utilizes state-of-the-art BERT models for summarization, while the frontend allows users to interact with the summarization service seamlessly.

## Features

### Backend (Flask API)

- **BERT-based Summarization:** Utilizes state-of-the-art BERT models for extracting key information from documents.
- **Flask API:** Built on Flask, providing a RESTful API for easy integration into web applications or services.
- **Cross-Origin Resource Sharing (CORS):** Allows for secure cross-origin communication, making it accessible from different domains.

### Frontend (React)

- **User-Friendly Interface:** Clean and intuitive interface for users to interact with the text summarization service.
- **File Upload Support:** Allows users to upload documents in various formats for summarization.
- **Real-time Summarization:** Displays the summarized text in real-time for immediate user feedback.

## Getting Started

### Prerequisites

- Python 3.x
- Pipenv (optional but recommended)
- Node.js and npm (for the React frontend)

### Backend Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/text-summarizer.git
   cd text-summarizer/backend
Install dependencies:

bash
Copy code
pipenv install
Run the Flask application:

bash
Copy code
pipenv run python app.py
The backend API will be available at http://localhost:5000.

Frontend Installation
Navigate to the frontend directory:

bash
Copy code
cd ../frontend
Install dependencies:

bash
Copy code
npm install
Run the React development server:

bash
Copy code
npm start
The frontend will be available at http://localhost:3000.

Usage
Open your web browser and go to http://localhost:3000.
Upload a document for summarization using the provided interface.
Receive the summarized text in real-time.
API Endpoint
Endpoint: /summarize
Method: POST
Request Body:

json
Copy code
{
    "documentContent": "Your long document text goes here..."
}
Response:

json
Copy code
{
    "summary": "Your summarized text..."
}
Example:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"documentContent": "Lorem ipsum dol
