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
    def save2file(self, data):
        pass

# PATH = Path(Path(__file__).parent.parent, 'data', 'sj.json')


class Save2json(AbstractSave):
    """
    Class to save a vacancy to a json file
    """
    # path_json = Path(Path(__file__).parent.parent, 'data', 'vacancy.json')

    def save2file(self, data):
        path_json = Path(Path(__file__).parent.parent, 'data', 'vacancy.json')

        with open(path_json, 'w', encoding='utf8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)
    #
    # def save_as_json(self, data):
    #     with open("../vacancies.json", "w", encoding="utf-8") as file:
    #         json.dump(data, file, sort_keys=False, indent=2, ensure_ascii=False)

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


if __name__ == '__main__':
    v = {'hr_platform': 'SuperJob', 'keyword': 'py', 'top_n_vacancies': 2}
    saver = Save2json()
    saver.save2file(v)
