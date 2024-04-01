import requests

class Apicopmany:

    def get_industry(self, company_id):
        """
       Метод класса получает информацию о компании по id
        """
        url = f'https://api.hh.ru/employers/{company_id}'
        response = requests.get(url)
        data = response.json()
        return {'company_id': data['id'], 'company_name': data['name']}
