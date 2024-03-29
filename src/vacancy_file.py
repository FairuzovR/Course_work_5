import requests

company_id = [675794, 562530, 3148, 1276, 1552384, 78638, 1346,  23435, 4934, 20986]

def validate_salary(salary, key):
    """Метод проверяет указана ли зарплата и отдает 0 в случае None"""
    if key == 'from':
        if salary is None:
            return None
        else:
            if salary['from'] is None and salary['to'] is not None:
                return 0
            else:
                return salary['from']
    if key == 'to':
        if salary is None:
            return None
        else:
            if salary['to'] is None and salary['from'] is not None:
                return 0
            else:
                return salary['to']


class Apivacancy:

    def __init__(self, company_id):
        self.company_id = company_id

    def get_vacancyes_company(self):
        """
        Функция для получения данных компании по интентификатору
        """
        data_list = list()
        url = f'https://api.hh.ru/vacancies?employer_id={self.company_id}'
        response = requests.get(url)
        data = response.json()
        # return data['items']
        for temp in data['items']:
            data_list.append({'vacancy_id': temp['id'], 'vacancy_name': temp['name'],
                              'salary_from': validate_salary(temp['salary'], 'from'),
                              'salary_to': validate_salary(temp['salary'], 'to'),
                              'url_vacancy': temp['alternate_url'],
                              'company_id': temp['employer']['id'],
            })
        return data_list

# a = Apivacancy(562530)
# print(a.get_vacancyes_company())
