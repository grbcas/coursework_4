from src.vacancy import *
from src.api import *
from src.utils import *
from src.save2file import *

iu = interact_user()
# iu = {'hr_platform': 'SuperJob', 'keyword': 'py', 'n_vacancies': 20, 'vacancies_sorted': True}

sj = ParserSJ('python')
data = sj.get_vacancy()

vacancies = []
for i_vacancy in data:
    profession = i_vacancy['profession']
    salary = i_vacancy['salary']
    link = i_vacancy['link']
    currency = i_vacancy['currency']

    vacancies.append(Vacancy(profession, salary, link, currency))

vacancies.sort(reverse=True)

vacancies_to_file = []
for i_vacancy in vacancies:
    vacancies_to_file.append(i_vacancy.__dict__)

save2json = Save2json()
save2json.save2file(vacancies_to_file)

# save2json.add_vacancy(vacancies[0].__dict__)
# save2json.delete_vacancy(vacancies[0].__dict__)
top_n_vacancies = save2json.get_data_from_json(u_request=iu.get('top_n_vacancies'))
print(top_n_vacancies)
