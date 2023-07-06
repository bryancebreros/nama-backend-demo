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
# Upload N files 
POST
Endpoint: /files
content-Type: multipart/form-data
body: 
    files: file1.pdf
    files: file2.pdf
    files: fileN.pdf
    ...
# Delete a file 
DELETE
Endpoint: files/
content-Type: application/json
body: {
    "files": [ "file1.pdf","file2.pdf","fileN.pdf" ]
}
# Get files in context
GET
Endpoint: /files