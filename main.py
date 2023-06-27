from flask import Flask
from flask_restful import Api
from app.routes.ChatGPT import ChatGPT

app = Flask(__name__)
api = Api(app)


api.add_resource(ChatGPT, '/question')

if __name__ == '__main__':
    app.run(debug=True)
