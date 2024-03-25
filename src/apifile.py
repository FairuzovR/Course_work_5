# from abc import ABC, abstractmethod
import requests

company_id = {
    'УМПО': 675794, 'Фармленд' : 562530, 'СИТИЛИНК' : 3148, "Окей" : 1276, "Додо Пицца" : 1552384,
    'Тинькофф' : 78638, 'Черкизово' : 1346,  'Профи' : 23435, 'Билайн' : 4934, 'Алиди' : 20986

}

class Apifile:

    def __init__(self, company_id):
        self.company_id = company_id

    def get_industry(self):
        """
        Функция для получения данных компании по интентификатору
        """
        url = f'https://api.hh.ru/employers/{self.company_id}'
        response = requests.get(url)
        data = response.json()
        return data
        # print(data)

# get_industry(675794)

    def get_vacancyes_company(self):

        url = f'https://api.hh.ru/vacancies?employer_id={self.company_id}'
        response = requests.get(url)
        data = response.json()
        return data
        # print(data)


ABS = Apifile(675794)

print(ABS.get_vacancyes_company())