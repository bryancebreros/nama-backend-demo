from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from app.modules.embedings import Embeddings
from langchain.llms import OpenAIChat

load_dotenv()


class Prompt:
    context = None
    db = None
    qa = None

    def __init__(self):
        self.context = False
        self.documents = self.context

        if self.documents:
            self.db = Embeddings.updateEmbeddings(self.documents)
        else:
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
