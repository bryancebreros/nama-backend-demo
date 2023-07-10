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
            return True

        array_json = result[0]
        old_files = json.loads(array_json)
        if set(new_files) != set(old_files):
            files_json = json.dumps(new_files)
            cursor.execute("UPDATE file SET elements = ? WHERE id = 1", (files_json,))
            conn.commit()
            conn.close()
            print("Context has been updated!")
            return True
        print("No updates in context.")
        conn.close()
        return False

    def getFiles(self):
        files = glob.glob("app/static/*")
        new_files = [file_name.replace("app/static/", "") for file_name in files]
        print(new_files)


