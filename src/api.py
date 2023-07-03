from abc import ABC, abstractmethod
import requests
import os


class Api(ABC):
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def get_vacancy(self):
		pass


class ParserSJ(Api):
	api_key: str = os.getenv('SUPERJOB_TOKEN')
	headers: str = {'X-Api-App-Id': api_key}

	def __init__(self, keyword, n_vacancies=5):
		self.keyword: str = keyword
		self.n_vacancies: int = n_vacancies

		self.api_url = 'https://api.superjob.ru/2.0/vacancies/'
		self.params = {
			"count": 20,
			"page": 0,
			"keyword": self.keyword,
			"archive": False
			}

	def get_vacancy(self):
		# print(self.keyword)
		api_url = f'https://api.superjob.ru/2.0/vacancies/?'

		sj_data = requests.get(api_url, headers=self.headers, params=self.params).json()

		sj_vacancies = []
		for vacancy in sj_data['objects']:
			keys_vacancy = {
				'platform': "SuperJob",
				'profession': vacancy['profession'],
				'salary': vacancy['payment_from'],
				'link': vacancy['link'],
				'currency': vacancy["currency"]
				}
			sj_vacancies.append(keys_vacancy)

		return sj_vacancies


class ParserHH(Api):

	def __init__(self, keyword):
		self.keyword = keyword
		self.api_url = f'https://api.hh.ru/vacancies?text={self.keyword}'
		self.params = {
			"per_page": 20,
			"page": 0,
			"archived": False
		}
		self.header = {"User_Agent": "HHScalperApp 1.0"}
		self.vacancies = []

	def get_vacancy(self):
		"""
		Load vacancies
		:return:
		"""
		hh_vacancies = []
		hh_data = requests.get(self.api_url, headers=self.header, params=self.params).json()
		# if hh_data.status_code != 200:
		# 	raise requests.ConnectionError(f"Error while trying to get Vacancies!")
		for vacancy in hh_data['items']:
			try:
				keys_vacancy = {
					'platform': "HeadHunter",
					'profession': vacancy['name'],
					'salary': vacancy.get('salary', 99).get('from', 0),
					'link': vacancy['alternate_url'],
					'currency': vacancy['salary']["currency"]
				}
			except AttributeError:
				keys_vacancy = {
					'platform': "HeadHunter",
					'profession': vacancy['name'],
					'salary': 0,
					'link': vacancy['alternate_url'],
					'currency': 'RUB'
				}

			hh_vacancies.append(keys_vacancy)

		return hh_vacancies
