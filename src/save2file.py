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

PATH = Path(Path(__file__).parent.parent, 'data', 'vacancy.json')


class AbstractSave(ABC):

    @abstractmethod
    def save2file(self, data):
        pass


class Save2json(AbstractSave):
    """
    Class to write/get data from a json file
    """

    def save2file(self, data, path_json=PATH):
        """
        save vacancies to a json file
        :param data:
        :param path_json:
        :return:
        """
        with open(path_json, 'w', encoding='utf8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)

    def add_vacancy(self, new_data, path_json=PATH):
        """
        Add data to a json file
        :param new_data:
        :param path_json:
        :return:
        """
        with open(path_json, 'r', encoding='utf8') as json_file:
            data = self.get_data_from_json()
            print(len(data))
            data.append(new_data)
            print(len(data))
        with open(path_json, 'w', encoding='utf8') as json_file:
            print(data)
            json.dump(data, json_file, indent=2, ensure_ascii=False)

    def delete_vacancy(self, new_data, path_json=PATH):
        """
        Add data to a json file
        :param new_data:
        :param path_json:
        :return:
        """
        with open(path_json, 'r', encoding='utf8') as json_file:
            data: list = self.get_data_from_json()
            print(len(data))
            data.remove(new_data)
            print(len(data))
        with open(path_json, 'w', encoding='utf8') as json_file:
            print(data)
            json.dump(data, json_file, indent=2, ensure_ascii=False)

    def get_data_from_json(self, path_json=PATH, u_request=1):
        """
        Load first N from a json file
        :param u_request:
        :param path_json:
        :return: list | str
        """
        try:
            with open(path_json, mode='r', encoding='UTF8') as f:
                data = json.load(f)
            if u_request:
                return data[:u_request]
        except FileNotFoundError:
            return f'The file is not present'


if __name__ == '__main__':
    v = {'hr_platform': 'SuperJob', 'keyword': 'py', 'top_n_vacancies': 2}
    saver = Save2json()
    saver.save2file(v)
