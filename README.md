# nama-backend
Answer questions with  chatGPT 3.5 using pdfs as context 
# Ask a question
POST
Endpoint: /question
content-Type: application/json
body: {
    "question": "your question"
    "documentation": "1" (1 for consulting into documents or 0 if not)
}
# Upload a file 
POST
Endpoint: /files
content-Type: multipart/form-data
body: 
    file: file.pdf
# Delete a file 
DELETE
Endpoint: files/<file_name>
# Get files in context
GET
Endpoint: /files