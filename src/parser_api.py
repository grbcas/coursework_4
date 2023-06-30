from api import *
import requests
import os
# from pathlib import Path

# class ParserHH(Api):
# 	def get_vacancy(self):
# 		data = requests.get('https:/api.hh.ru/vacancies/').json()
# 		return data


class ParserSJ(Api):
	api_key: str = os.getenv('SUPERJOB_TOKEN')
	headers: str = {'X-Api-App-Id': api_key}

	def __init__(self, keyword):
		self.keyword: str = keyword

	def get_vacancy(self):
		print(self.keyword)
		api_url = f'https://api.superjob.ru/2.0/vacancies/?' \
				f'keyword={self.keyword}&' \
				f'count=5'

		sj_data = requests.get(api_url, headers=self.headers).json()

		return sj_data['objects']


class Vacancy:
	"""
	Создать класс для работы с вакансиями.
	В этом классе самостоятельно определить атрибуты:
	 название вакансии,
	 ссылка на вакансию,
	 зарплата,
	 краткое описание или требования и т.п. (не менее четырех)
	Класс должен поддерживать методы сравнения вакансий между собой по зарплате
	 и валидировать данные, которыми инициализируются его атрибуты
	"""
	def __init__(self, profession, salary, link, requirements, currency):
		self.profession = profession
		self.__salary = salary
		self.link = link
		self.requirements = requirements
		self.currency = currency

	@property
	def salary(self):
		return self.__salary

	@salary.setter
	def salary(self, salary):
		if salary == 0:
			self.__salary = 50000
		else:
			rate = self.get_exchange_rate(self.currency)
			# rate = 1
			self.__salary = salary * rate

	@staticmethod
	def get_exchange_rate(currency):
		rate = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
		return rate['Valute'][currency]['Value']


	@classmethod
	def __verify_data(cls, other):
		if not isinstance(other, int | Vacancy):
			raise TypeError("The operand must have the type int or Vacancy")
		return other if isinstance(other, int) else other.salary

	def __eq__(self, other):
		sc = self.__verify_data(other)
		return self.salary == sc

	def __gt__(self, other):
		sc = self.__verify_data(other)
		return self.salary > sc

	def __lt__(self, other):
		sc = self.__verify_data(other)
		return self.salary < sc


if __name__ == '__main__':
	iu = {'hr_platform': 'SuperJob', 'keyword': 'py', 'top_n_vacancies': 2, 'vacancies_sorted': True}

	sj = ParserSJ('python')
	data = sj.get_vacancy()
	print(len(data))
	with open('sj.json', mode='w', encoding='utf8') as f:
		# f.write(data)
		print(data, file=f)
