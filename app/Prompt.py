from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from app.modules.embedings import Embeddings
from langchain.llms import OpenAIChat
from app.modules.context import FolderSearch
from langchain.document_loaders import PyPDFDirectoryLoader

load_dotenv()


class Prompt:
    context = False
    db = None
    qa = None

    def __init__(self):
        # self.context = FolderSearch()
        # self.documents = self.context.check_for_new_document()
        try:
            if self.checkContext() == False:
                self.db = Embeddings.getEmbeddings()
            self.qa = RetrievalQA.from_chain_type(
                llm=OpenAIChat(model="gpt-3.5-turbo"),
                chain_type="stuff",
                retriever=self.db.as_retriever(),
            )
        except Exception as e:
            print("Error: ", e)

    def checkContext(self):
        self.context = FolderSearch().check_for_new_document()
        print("context: ", self.context)
        if self.context:
            loader = PyPDFDirectoryLoader("app/static")
            docs = loader.load()
            print("entró al if")
            self.db = Embeddings.updateEmbeddings(docs)
            return True
        else:
            print("no entró")
            return False

    def query(self, question):
        return self.qa.run(question)

    def ask(self, question):
        return self.llm_chain.run(question)
