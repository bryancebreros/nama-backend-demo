from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFDirectoryLoader

load_dotenv()

# loads context by reading all pdfs in the "context" folder
try:
    loader = PyPDFDirectoryLoader("context")
   
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    # we ask OpenAI for the embeddings of our document and we load them
    # into a chroma database
    docsearch = Chroma.from_documents(texts, embeddings)
except Exception:
    print("error while loading context ")

else:
    print("context loaded successfully")

    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(client="nama"),
        chain_type="stuff",
        retriever=docsearch.as_retriever(search_kwargs={"k": 1}),
    )

    while True:
        query = input(
            """Please enter your request or type "exit":
    """
        )

        if query == "exit":
            break
        if query == "demo":
            demo = "What's the difference between contacts and registrants?"
            print(demo)
            query = demo
        print("A:", qa.run(query))

# query = """which are the three types of questions I
# can ask in a survey or poll?"""

# query2 = """can you give me an example of
# the multiple choice type of question?"""

# print("Q:", query)
# print("A:", qa.run(query))
# print("Q:", query2)
# print("A:", qa.run(query2))
