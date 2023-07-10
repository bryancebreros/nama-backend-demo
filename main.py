from flask import Flask
from flask_restful import Api
from app.routes.ChatGPT import ChatGPT
from app.routes.Files import Files
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(ChatGPT, "/question")
# api.add_resource(Files, "/upload")
# api.add_resource(Files, "/files/<string:file_name>")
api.add_resource(Files, "/files", endpoint="upload")
api.add_resource(Files, "/files/<string:file_name>", endpoint="delete")
if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
