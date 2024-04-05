import os
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from config import directory_path


class FileListApi(APIView):

    def get(self, request):
        files_info = []
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            file_time = os.path.getmtime(file_path)
            file_info = {
                "name": file_name,
                "type": "file",
                "time": datetime.fromtimestamp(file_time).strftime('%Y-%m-%d %H:%M:%S')
            }
            files_info.append(file_info)
        return Response({"data": files_info})
