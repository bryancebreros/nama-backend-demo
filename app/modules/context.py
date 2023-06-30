#cargar lo que hay en base de datos 
#investigar cómo calcular el hash y ver si ya hay un nuevo documento, funcion que retorna 
import os
import glob
import json
import sqlite3
from langchain.document_loaders import PyPDFDirectoryLoader



conn = sqlite3.connect('database.db')
cursor = conn.cursor()

class FolderSearch:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def check_for_new_document(self):
        os.chdir(self.folder_path)
        new_files = glob.glob('*')
        new_files = ['go']
        print(new_files)
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS file (
                    id INTEGER PRIMARY KEY,
                    elements TEXT
                )
            ''')
        cursor.execute("SELECT elements FROM file")
        result = cursor.fetchone()
        print('r', result)
        if result is None:
            print('entro')
            files_json = json.dumps(new_files)
            cursor.execute("INSERT INTO file (elements) VALUES (?) WHERE id = 0 ", (files_json,))  
            conn.commit()
            conn.close()
        

        array_json = result[0]
        old_files = json.loads(array_json)
        if set(new_files) != set(old_files):
            files_json = json.dumps(new_files)
            cursor.execute("UPDATE file SET elements = ? WHERE id = 1", (files_json,))
            conn.commit()
            conn.close()
            print('Context has been updated!')
            loader = PyPDFDirectoryLoader(folder_path)
            documents = loader.load()
            return documents
            # print('diferentes')
            # return True
        conn.close()
        return False
            
           
        


folder_path = '../static'

folder_search = FolderSearch(folder_path)

folder_search.check_for_new_document()

# if has_new_document:
#     print("There is a new document in the folder.")
# else:
#     print("No new document found in the folder.")


#Clase que carga lo que hay de base de datos
#Checa si hay un cambio para reacalcular
#retorna los documentos parseados