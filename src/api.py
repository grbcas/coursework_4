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

	def __init__(self, keyword):
		self.keyword: str = keyword

	def get_vacancy(self):
		print(self.keyword)
		api_url = f'https://api.superjob.ru/2.0/vacancies/?' \
				f'keyword={self.keyword}&' \
				f'count=5'

		sj_data = requests.get(api_url, headers=self.headers).json()

		return sj_data['objects']

# class ParserHH(Api):
# 	def get_vacancy(self):
# 		data = requests.get('https:/api.hh.ru/vacancies/').json()
# 		return data