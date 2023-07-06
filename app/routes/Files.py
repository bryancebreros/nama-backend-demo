from flask_restful import Resource, reqparse
import werkzeug
import os
import glob


fileType = werkzeug.datastructures.FileStorage


class Files(Resource):
    # def post(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument("file", type=fileType, location="files", required=True)
    #     args = parser.parse_args()
    #     fileArg = args["file"]
    #     folder = "app/static"
    #     if not os.path.exists(folder):
    #         print("no exists")
    #         os.makedirs(folder)
    #     # file_name = werkzeug.utils.secure_filename(fileArg.filename)
    #     # file_route = os.path.join(folder, file_name)
    #     file_name = fileArg.filename
    #     file_route = os.path.join(folder, file_name)
    #     fileArg.save(file_route)
    #     return {"message": "File received"}
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "files", type=fileType, location="files", action="append", required=True
        )
        args = parser.parse_args()
        files = args["files"]
        file_names = []
        folder = "app/static"
        if not os.path.exists(folder):
            os.makedirs(folder)
        for file in files:
            file_name = file.filename
            file_names.append(file_name)
            file_path = os.path.join(folder, file_name)
            file.save(file_path)
        return {"message": "Files received", "file_names": file_names}

    def delete(self, file_name):
        # print(file_name)
        # return {"message": file_name}
        folder = "app/static"
        file_route = os.path.join(
            folder,
            file_name + ".pdf",
        )
        # print(file_route)
        # Verificar si el archivo existe
        if os.path.isfile(file_route):
            # Eliminar el archivo
            os.remove(file_route)
            return {"message": "File deleted"}
        else:
            return {"message": "File not found"}, 404

    def get(self):
        files = glob.glob("app/static/*")
        new_files = [file_name.replace("app/static/", "") for file_name in files]
        return {"files": new_files}
