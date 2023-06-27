from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFDirectoryLoader
load_dotenv()

class Prompt:
    def __init__(self):
        #Chat
        self.qa = False
        self.template = """Question: {question}
        Answer: Let's think step by step."""
        self.prompt = PromptTemplate(template=self.template, input_variables=["question"])
        self.llm = OpenAI(temperature=0.9)
        self.llm_chain = LLMChain(prompt=self.prompt, llm=self.llm)

        try:
            #contexto
            self.loader = PyPDFDirectoryLoader("app/static")
            self.documents = self.loader.load()
            #embedings
            self.text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            self.texts = self.text_splitter.split_documents(self.documents)
            self.embeddings = OpenAIEmbeddings(client="nama")
            self.docsearch = Chroma.from_documents(self.texts, self.embeddings)

        except Exception:
            print("error while loading context")

        else:
            print("context loaded successfully")
            #Chat
            self.qa = RetrievalQA.from_chain_type(
                llm=OpenAI(client="nama"),
                chain_type="stuff",
                retriever= self.docsearch.as_retriever(search_kwargs={"k": 1}),
            )
    def query(self, question):
        return self.qa.run(question)
    def ask(self, question):
        return self.llm_chain.run(question)
