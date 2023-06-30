from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from app.modules.embedings import Embeddings
from langchain.llms import OpenAIChat
from app.modules.context import FolderSearch

load_dotenv()


class Prompt:
    context = False
    db = None
    qa = None

    def __init__(self):
        self.context = FolderSearch()
        self.documents = self.context.check_for_new_document()

        if self.documents:
            print("entró al if")
            self.db = Embeddings.updateEmbeddings(self.documents)
        else:
            print("no entró")
            self.db = Embeddings.getEmbeddings()

        self.qa = RetrievalQA.from_chain_type(
            llm=OpenAIChat(model="gpt-3.5-turbo"),
            chain_type="stuff",
            retriever=self.db.as_retriever(),
        )

    def query(self, question):
        return self.qa.run(question)

    def ask(self, question):
        return self.llm_chain.run(question)
