# nama-backend
Answer questions with  chatGPT 3.5 using pdfs as context 

# Installation

- install and setup [asdf](https://asdf-vm.com/guide/getting-started.html).
- install asdf's python plugin [dependencies](https://github.com/pyenv/pyenv/wiki#suggested-build-environment).
- install asdf's [python plugin](https://github.com/asdf-community/asdf-python).

        asdf plugin-add python
  (see `.tools-versions` for the version we are using).
- install asdf's [direnv](https://github.com/asdf-community/asdf-direnv) plugin:

      asdf plugin-add direnv
      asdf direnv setup --shell bash --version latest
  (change `bash` for your preferred shell)
- install the python using asdf's plugin using the following command on the root of the project
  
        asdf python install
- create a python virtual environment called `venv` on the project's root directory:

      python3 -m venv venv
  or

      python -m venv venv
  depending on your OS.
- activate the virtual environment with

        source venv/bin/activate
- create a `.env` file with the api key for OpenAI:
  - it should have one line with the following structure
  - `OPENAI_API_KEY="api key"`
- install python requirements with pip

        pip install -r requirements.txt

## Usage

- place PDFs to be used as context in `app/static/`
- start the app with:

        flask --app main.py run

## Requests
### Ask a question
    POST
    Endpoint: /question
    content-Type: application/json
    body: {
        "question": "your question"
        "documentation": "1" 
    }
(1 for consulting using PDFs or 0 if not)

### Upload N files 
    POST
    Endpoint: /files
    content-Type: multipart/form-data
    body: 
        files: file1.pdf
        files: file2.pdf
        files: fileN.pdf
        ...
    
### Delete a file 
    DELETE
    Endpoint: files/
    content-Type: application/json
    body: {
        "files": [ "file1.pdf","file2.pdf","fileN.pdf" ]
    }

### Get files in context
    GET
    Endpoint: /files
