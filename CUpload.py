# App Class User!
# @author: Dr. Benjamin M. Abdel-Karim
# @since: 2022-01-21
# @version: 2022-01-21 - Alpha 2021-07-21.20:22

from datetime import datetime
from uuid import uuid4
import os

class CUpload():
    def __init__(self, sUpload_path, request):
        # Generate unique ID by using uuid
        # @source: https://stackoverflow.com/questions/50368143/create-unique-id-based-on-date-in-python
        # self.hash_id = datetime.now().strftime('%Y-%m-%d-%H:%M:%S-') + str(uuid4())
        self.hash_id = datetime.now().strftime('%Y-%m-%d-') + str(uuid4())

        # # Upload
        self.upload = request.form.get('upload')

        # Upload Function and storage for the File upload. Create a extra Folder with hash/id
        file = request.files.get('upload')
        sSubfolder_path = sUpload_path + str(self.hash_id)
        if not os.path.exists(sSubfolder_path):
            os.makedirs(sSubfolder_path)


        file.save(os.path.join(sSubfolder_path, file.filename))

        self.upload_path = os.path.join(sSubfolder_path, file.filename)
