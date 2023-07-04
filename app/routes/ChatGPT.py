from flask_restful import Resource, reqparse
from app.Prompt import Prompt


class ChatGPT(Resource):
    prompt = Prompt()

    def post(self):
        self.prompt.checkContext()
        parser = reqparse.RequestParser()
        parser.add_argument("question", type=str, required=True)
        parser.add_argument("documentation", type=str, required=True)
        args = parser.parse_args()
        print("args", args)
        question = args["question"]
        documentation = args["documentation"]
        if documentation == "1":
            response = self.prompt.query(question)
        else:
            response = self.prompt.ask(question)
        return {"question": question, "response": response}
