from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.llms import OpenAIChat

load_dotenv()

# Load all the Python project files using the PyPDFDirectoryLoader
loader = PyPDFDirectoryLoader("app/static")
docs = loader.load_and_split()
print(docs)
# Chunk the documents using the CharacterTextSplitter
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = splitter.split_documents(docs)
# Embeddings model
embeddings = OpenAIEmbeddings()
# db = DeepLake.from_documents(texts, dataset_path="./my_deeplake/", embedding=embeddings, overwrite=True)
# db = DeepLake(
#     dataset_path="./my_deeplake/", embedding_function=embeddings, overwrite=True
# )
# db.add_documents(texts)
db = DeepLake(
    dataset_path="./my_deeplake/", embedding_function=embeddings, read_only=True
)
# qa = RetrievalQA.from_chain_type(
#     llm=OpenAIChat(model="gpt-3.5-turbo"),
#     chain_type="stuff",
#     retriever=db.as_retriever(),
# )
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(client="nama"),
    chain_type="stuff",
    retriever=db.as_retriever(),
)
query = "How can I create a poll or a survey for my event?"
print(qa.run(query))
