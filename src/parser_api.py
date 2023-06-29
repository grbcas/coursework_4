from vacancy import *
import requests
import os
# from pathlib import Path

# class ParserHH(Vacancy):
# 	def get_vacancy(self):
# 		data = requests.get('https:/api.hh.ru/vacancies/').json()
# 		return data


class ParserSJ(Vacancy):
	api_key: str = os.getenv('SUPERJOB_TOKEN')
	headers: str = {'X-Api-App-Id': api_key}

	def __init__(self, keyword):
		self.keyword: str = keyword

	def get_vacancy(self):
		print(self.keyword)
		api_url = f'https://api.superjob.ru/2.0/vacancies/?' \
				f'keyword={self.keyword}&' \
				f'count=1'

		sj_data = requests.get(api_url, headers=self.headers).json()

		return sj_data['objects']


class Vacancy:
	def __init__(self, salary):
		self.salary = salary

	def __gt__(self, other):
		if other.salary > self.salary:
			return True

	def __eq__(self, other):
		if other.salary == self.salary:
			return True

	def __lt__(self, other):
		if other.salary < self.salary:
			return True


if __name__ == '__main__':
	iu = {'hr_platform': 'SuperJob', 'keyword': 'py', 'top_n_vacancies': 2, 'vacancies_sorted': True}

	sj = ParserSJ('python')
	data = sj.get_vacancy()
	print(len(data))
	with open('sj.json', mode='w', encoding='utf8') as f:
		# f.write(data)
		print(data, file=f)
