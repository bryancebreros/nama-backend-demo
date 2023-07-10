from flask_restful import Resource, reqparse
import werkzeug
import os
import glob


fileType = werkzeug.datastructures.FileStorage


class Files(Resource):
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

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("files", type=str, action="append", required=True)
        args = parser.parse_args()
        files = args["files"]
        folder = "app/static"
        deleted = []
        for file in files:
            file_route = os.path.join(folder, file)
            if os.path.isfile(file_route):
                os.remove(file_route)
                deleted.append(file)
        return {"message": "Files deleted", "deleted": deleted}

    def get(self):
        files = glob.glob("app/static/*")
        new_files = [file_name.replace("app/static/", "") for file_name in files]
        return {"files": new_files}