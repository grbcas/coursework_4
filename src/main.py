from src.vacancy import *
from src.api import *
from src.utils import *
from src.save2file import *

# iu = interact_user()
iu = {'hr_platform': 'SuperJob', 'keyword': 'py', 'top_n_vacancies': 2, 'vacancies_sorted': True}


sj = ParserSJ('python')
data = sj.get_vacancy()
with open('sj.json', mode='w', encoding='utf8') as f:
    # f.write(data)
    print(data, file=f)

vacancies = []
for i_vacancy in data:
    profession = i_vacancy['profession']
    salary = i_vacancy['payment_from']
    link = i_vacancy['link']
    requirements = i_vacancy['candidat']
    currency = i_vacancy['currency']

    vacancies.append(Vacancy(profession, salary, link, requirements, currency))

vacancy = vacancies[0]
print(vacancy)
# print(vacancies[0].salary)
# vacancies[0].salary = 0
# print(vacancies[0].salary)

Save2json.save2file(vacancy)
