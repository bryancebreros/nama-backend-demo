# cargar lo que hay en base de datos
# investigar cómo calcular el hash y ver si ya hay un nuevo documento, funcion que retorna
import os
import glob
import json
import sqlite3
from langchain.document_loaders import PyPDFDirectoryLoader


class FolderSearch:
    def __init__(self, folder_path="app/static"):
        print(folder_path)
        self.folder_path = folder_path

    def check_for_new_document(self):
        print(self.folder_path)
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        # os.chdir(self.folder_path)
        # os.chdir("app/static")
        new_files = glob.glob("app/static/*")
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS file (
                    id INTEGER PRIMARY KEY,
                    elements TEXT
                )
            """
        )
        cursor.execute("SELECT elements FROM file")
        result = cursor.fetchone()
        if result is None:
            files_json = json.dumps(new_files)
            cursor.execute("INSERT INTO file (elements) VALUES (?) ", (files_json,))
            conn.commit()
            conn.close()
            print("Context has been created!")
            print(self.folder_path)
            # loader = PyPDFDirectoryLoader(self.folder_path)
            # loader = PyPDFDirectoryLoader("app/static")
            # documents = loader.load()
            # return documents
            # os.chdir("../..")
            return True

        array_json = result[0]
        old_files = json.loads(array_json)
        if set(new_files) != set(old_files):
            files_json = json.dumps(new_files)
            cursor.execute("UPDATE file SET elements = ? WHERE id = 1", (files_json,))
            conn.commit()
            conn.close()
            print("Context has been updated!")
            # loader = PyPDFDirectoryLoader(self.folder_path)
            # loader = PyPDFDirectoryLoader("app/static")
            # documents = loader.load()
            # print(documents)
            # return documents
            # os.chdir("../..")
            return True
        print("No updates in context.")
        conn.close()
        return False


# folder_search = FolderSearch()

# folder_search.check_for_new_document()

# if has_new_document:
#     print("There is a new document in the folder.")
# else:
#     print("No new document found in the folder.")


# Clase que carga lo que hay de base de datos
# Checa si hay un cambio para reacalcular
# retorna los documentos parseados
