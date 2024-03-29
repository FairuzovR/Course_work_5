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


    def get_vacancyes_company(self):

        url = f'https://api.hh.ru/vacancies?employer_id={self.company_id}'
        response = requests.get(url)
        data = response.json()
        return data
        # print(data)

    @staticmethod
    def write_company_for_joisn(file):
        """Метод выводит словари с нужными данными в итерации списка экземпляров класса
        и записывает их в словарь для дальнейший записи в json файл"""
        data_list = []
        for temp in file:
            data_list.append({'company_id': temp['id'], 'company_name': temp['name']})
        return data_list

    @staticmethod
    def write_vacancy_for_joisn(file):
        data_list = []
        for temp in file:
            data_list.append({'vacancy_id': temp['id'], 'vacancy_name': temp['name'], 'city' : temp['area']['name'],
                              'salary_from' : temp['salary']['from'], 'salary_to' : temp['salary']['to'],
                              'url_vacancy' : temp['apply_alternate_url'], 'company_id' : temp['employer']['id']})
        return data_list


ABS = Apifile('23435')
#
print(ABS.get_vacancyes_company())
# a = ABS.get_vacancyes_company()['items']
# for i in a:
#     print(i)
# print(ABS.get_vacancyes_company())
