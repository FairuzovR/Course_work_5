import requests

company_id = [675794, 562530, 3148, 1276, 1552384, 78638, 1346,  23435, 4934, 20986]

class Apicopmany:
    def __init__(self, company_id):
        self.company_id = company_id

    def get_industry(self):
        """
        Функция для получения данных компании по интентификатору
        """
        url = f'https://api.hh.ru/employers/{self.company_id}'
        response = requests.get(url)
        data = response.json()
        return {'company_id': data['id'], 'company_name': data['name']}
# def from_class_info(dict_file):
#
#         return {'company_id': dict_file['id'], 'company_name': dict_file['name']}


# a = Apicopmany('675794')
# print(a.get_industry())