from flask import Flask, request, jsonify
from flask_cors import CORS
from summarizer import Summarizer  

app = Flask(__name__)
CORS(app)

summarizer = Summarizer()

@app.route('/summarize', methods=['POST'])
def summarize_document():
    data = request.get_json()
    document_content = data.get('documentContent', '')

    # Using bert-extractive-summarizer
    summary = summarizer(document_content, ratio=0.2)  

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)


