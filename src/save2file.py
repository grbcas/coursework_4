"""
# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
json_saver.delete_vacancy(vacancy)
"""
from abc import ABC, abstractmethod
from pathlib import Path
import json


class AbstractSave(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def save2file(self):
        pass

# PATH = Path(Path(__file__).parent.parent, 'data', 'sj.json')


class Save2json(AbstractSave):
    """
    Class to save a vacancy to a json file
    """
    # path_json = Path(Path(__file__).parent.parent, 'data', 'vacancy.json')

    def __init__(self, data):
        self.data: dict = data
        self.path_json = Path(Path(__file__).parent.parent, 'data', 'vacancy.json')

    def save2file(self):
        with open(self.path_json, 'w') as json_file:
            json.dump(self.data, json_file)

    def get_data_from_json(self: Path) -> list | str:
        """
        Load data from json file
        :param path_to_json_file:
        :return: list | str
        """
        try:
            with open(self, mode='r', encoding='UTF8') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            return f'The file is not present'
