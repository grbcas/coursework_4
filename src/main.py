from src.vacancy import Vacancy
from src.api import ParserSJ, ParserHH
from src.utils import interact_user
from src.save2file import Save2json


def main():
    iu = interact_user()
    sj = ParserSJ('python')
    hh = ParserHH('python')

    data = []
    if iu.get('hr_platform') == 'HeadHunter':
        data = hh.get_vacancy()
    elif iu.get('hr_platform') == 'SuperJob':
        data = sj.get_vacancy()

    vacancies = []
    for i_vacancy in data:
        profession = i_vacancy['profession']
        salary = i_vacancy['salary']
        link = i_vacancy['link']
        currency = i_vacancy['currency']
        vacancies.append(Vacancy(profession, salary, link, currency))

    vacancies.sort(reverse=True)
    print(f'LOADED {len(vacancies)} vacancies')

    vacancies_to_file = []
    for i_vacancy in vacancies:
        vacancies_to_file.append(i_vacancy.__dict__)

    save2json = Save2json()
    save2json.save2file(vacancies_to_file)
    if iu.get('save_option'):
        print(*vacancies_to_file)

    top_n_vacancies = save2json.get_data_from_json(u_request=iu.get('top_n_vacancies'))

    print(f'The list of the top N vacancies: {len(top_n_vacancies)}')

    print(*top_n_vacancies)
# save2json.add_vacancy(vacancies[0].__dict__) #
# save2json.delete_vacancy(vacancies[0].__dict__)


if __name__ == '__main__':
    main()
