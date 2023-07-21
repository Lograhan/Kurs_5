import json


class File_manager:
    """
    Класс для работы с файлами .json
    """

    @staticmethod
    def open_file(file_name):
        """
        Метод для открытия файла. В атрибут принимает путь и имя для файла .json
        """
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def add_vac(file_name, data):
        """
        Метод для записи файла. В атрибут принимает путь и имя для файла .json
        """
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data))
