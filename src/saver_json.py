import os
from  config import root_path
from src.company_file import Apicopmany
from src.vacancy_file import Apivacancy
import json

company_idi = [675794, 562530, 3148, 1276, 1552384, 78638, 1346,  23435, 4934, 20986]

class SaveJson:

    def __init__(self, file_name):
        self.file_name = file_name

    def add_company(self, company):

        with open(os.path.join(root_path, self.file_name), 'w', encoding='UTF-8') as file_json:
                data = json.dumps(company, ensure_ascii=False, indent=2)
                file_json.write(data)

    def add_vacancy(self, vacancies_info):
        with open(os.path.join(root_path, self.file_name), 'w', encoding='UTF-8') as file_json:
            data = json.dumps(company_info['items'], ensure_ascii=False, indent=2)
            file_json.write(data)




a = SaveJson('companies.json')
b = list()

# for company in  company_idi:
#     company_ex = Apicopmany(company)
#     api_get = company_ex.get_industry()
#     b.append(api_get)
# print(b)
# a = SaveJson('companies.json')
# a.add_company(b)


for vacancy in company_idi:
    vacancy_ex = Apivacancy(vacancy)
    api_get = vacancy_ex.get_vacancyes_company()
    for  i in api_get:
        b.append(i)
#
a = SaveJson('vacancy.json')
a.add_company(b)

