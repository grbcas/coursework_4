import requests


class Vacancy:
	"""
	Класс для работы с вакансиями.
	Определить атрибуты:
	название вакансии,
	ссылка на вакансию,
	зарплата,
	валюта зарплаты
	Методы сравнения вакансий между собой по зарплате
	и валидировать данные, которыми инициализируются его атрибуты
	"""
	def __init__(self, profession, salary, link, currency):
		self.profession: str = profession
		self.currency: str = currency
		self.salary = salary
		self.link: str = link

	@property
	def salary(self):
		"""
		Return value for class attribute value
		:return: _salary
		"""
		return self._salary

	@salary.setter
	def salary(self, value):
		"""
		Set value for class attribute value
		:param value:
		:return:
		"""
		if not value:
			self._salary = 999
		else:
			self._salary = value * self.rate_currency()

	def rate_currency(self):
		"""
		Return currency rate
		:return:
		"""
		if self.currency.upper() == 'BYR':
			rate = self.get_exchange_rate('byn')
			return rate
		if self.currency.upper() not in ['RUR', 'RUB']:
			rate = self.get_exchange_rate(self.currency)
			return rate
		return 1

	@staticmethod
	def get_exchange_rate(currency):
		rate = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
		value = rate['Valute'][currency.upper()]['Value']
		nominal = rate['Valute'][currency.upper()]['Nominal']
		return round(value / nominal)

	@classmethod
	def __verify_data(cls, other):
		"""
		Check of the type: int or Vacancy
		:param other:
		:return:
		"""
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
		return f'{self.profession} {self.salary} {self.currency} {self.link} '
