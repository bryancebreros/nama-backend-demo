import traceback
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.vectorstores import DeepLake
from langchain.text_splitter import CharacterTextSplitter


load_dotenv()

flag = False
print("executin retrieval")
try:
    loader = PyPDFDirectoryLoader("app/static")
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    if flag:
        db = DeepLake.from_documents(
            texts, dataset_path="./my_deeplake/", embedding=embeddings, overwrite=True
        )
    else:
        db = DeepLake(
            dataset_path="./my_deeplake/", embedding_function=embeddings, read_only=True
        )
except Exception as e:
    # Print the exception message
    print("An error occurred:")
    print(e)

    # Print the traceback
    print("error while loading context ")
    traceback.print_exc()
else:
    print("context loaded successfully")

    # qa = RetrievalQA.from_chain_type(
    #     llm=OpenAI(client="nama"),
    #     chain_type="stuff",
    #     retriever=conn,  # Use SQLite connection as the retriever
    #     table_name="document_embeddings",
    # )
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(client="nama"),
        chain_type="stuff",
        retriever=db.as_retriever(),
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
