# Divide en pedazos los documentos parseados
# consulta a contexto si hay cambios para recalcular embedings
# si no, solo usa el que ya tenía
# Recibe
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from dotenv import load_dotenv

load_dotenv()


class Embeddings:
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    embeddings = OpenAIEmbeddings()

    @staticmethod
    def updateEmbeddings(documents):
        texts = Embeddings.splitter.split_documents(documents)
        db = DeepLake.from_documents(
            texts,
            dataset_path="./my_deeplake/",
            embedding=Embeddings.embeddings,
            overwrite=True,
        )
        return db

    @staticmethod
    def getEmbeddings():
        db = DeepLake(
            dataset_path="./my_deeplake/",
            embedding_function=Embeddings.embeddings,
            read_only=True,
        )
        return db
