import requests


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
		self.profession: str = profession
		self.currency: str = currency
		self.salary = salary
		self.link: str = link
		self.requirements: str = requirements


	@property
	def salary(self):
		return self._salary

	@salary.setter
	def salary(self, value):
		if value == 0:
			self._salary = 9999
			# print(f': {value} = {self._salary}')
		else:
			self._salary = value * self.convert_salary()

	def convert_salary(self):
		if self.currency != 'rub':
			rate = self.get_exchange_rate(self.currency)
			return rate
		return 1

	@staticmethod
	def get_exchange_rate(currency):
		rate = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
		return rate['Valute'][currency.upper()]['Value']

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

	def __str__(self):
		return f'{self.profession} {self._salary} {self.currency} {self.link} '
	# {self.requirements}


if __name__ == '__main__':
	iu = {'hr_platform': 'SuperJob', 'keyword': 'py', 'top_n_vacancies': 2, 'vacancies_sorted': True}

	# sj = ParserSJ('python')
	# data = sj.get_vacancy()
	# print(len(data))
	# with open('sj.json', mode='w', encoding='utf8') as f:
	# 	# f.write(data)
	# 	print(data, file=f)
	#
	# vacancies = []
	# for i_vacancy in data:
	# 	profession = i_vacancy['profession']
	# 	salary = i_vacancy['payment_from']
	# 	link = i_vacancy['link']
	# 	requirements = i_vacancy['link']
	# 	currency = i_vacancy['currency']
	#
	# 	vacancies.append(Vacancy(profession, salary, link, requirements, currency))
	#
	# print(vacancies[0])
