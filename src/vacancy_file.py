import requests

def validate_salary(salary, key):
    """Метод проверяет указана ли зарплата, если общее None, то передаст каждому None,
     если один из двух показателей salary None, то передаст 0
     """
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

    def get_vacancyes_company(self, company_id):
        """
        Метод класса для получения данных компании по интентификатору
        """
        data_list = list()
        url = f'https://api.hh.ru/vacancies?employer_id={company_id}'
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
