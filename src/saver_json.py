import os
from  config import root_path
import json

class SaveJson:

    def __init__(self, file_name):
        self.file_name = file_name

    def add_file_to_json(self, id):
        """
        Метод класса, который записает подаваемую информацию в файл json
        """

        with open(os.path.join(root_path, self.file_name), 'w', encoding='UTF-8') as file_json:
                data = json.dumps(id, ensure_ascii=False, indent=2)
                file_json.write(data)
