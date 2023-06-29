"""
Создать функцию для взаимодействия с пользователем.
Функция должна взаимодействовать с пользователем через консоль.
Самостоятельно придумать сценарии и возможности взаимодействия с пользователем.
Например, позволять пользователю указать:
 с каких платформ он хочет получить вакансии,
 ввести поисковый запрос,
 получить топ N вакансий по зарплате,
 получить вакансии в отсортированном виде,
 получить вакансии, в описании которых есть определенные ключевые слова, например "postgres" и т.п.
"""
from sys import stdin


def interact_user(_in=stdin):
    hr_platform = {0: 'HeadHunter', 1: 'SuperJob'}
    [print(key, ':', value, end="\n") for key, value in hr_platform.items()]
    while True:
        try:
            print('hr_platform >')
            input_ = _in.readline()
            if int(input_) in range(0, 2):
                hr_id = int(input_)
                print('hr_id =', hr_id)
                print(hr_platform.get(hr_id))
                break
            else:
                raise ValueError
        except ValueError:
            print('enter number in range(0, 1)')

    print('search_keyword')
    search_keyword = _in.readline().strip()

    top_n_vacancies = 0
    while True:
        try:
            print('top_n_vacancies >')
            input_ = _in.readline()
            if int(input_) in range(100):
                top_n_vacancies = int(input_)
                print('top_n_vacancies =', top_n_vacancies)
                break
            else:
                raise ValueError
        except ValueError:
            print('enter number in range(1, 99)')

    sort_vacancies = 0
    while True:
        try:
            print('sort_vacancies >')
            input_ = _in.readline()
            if int(input_) in range(0, 2):
                sort_vacancies = bool(int(input_))
                print('sort_vacancies =', sort_vacancies)
                break
            else:
                raise ValueError
        except ValueError:
            print('enter number in range(0, 1)')

    user_input = {'hr_platform': hr_platform.get(hr_id),
                  'keyword': search_keyword,
                  'top_n_vacancies': top_n_vacancies,
                  'vacancies_sorted': sort_vacancies}

    return user_input


if __name__ == '__main__':
    iu = interact_user()
    print(iu)