import psycopg2
from config import root_path
import os
import json

company_id = [675794, 562530, 3148, 1276, 1552384, 78638, 1346,  23435, 4934, 20986]

def validate_null(salary):
    if salary == "null":
        return null

class DBManager:

    def __init__(self, json_company, json_vacancy):
        self.json_company = json_company
        self.json_vacancy = json_vacancy
        self.conn = psycopg2.connect(host='localhost',
                                         database='hh_base',
                                         user='postgres',
                                         password='2162')
        self.cur =  self.conn.cursor()
    def create_table_companies(self):

        self.cur.execute ("CREATE TABLE company (company_id int PRIMARY KEY, company_name varchar(100) NOT NULL)")
        self.conn.commit()
        # self.cur.close()
        # self.conn.close()
        with open(os.path.join(root_path, self.json_company), 'r', encoding='utf-8') as r_file:
            raw_json = r_file.read()
            obj = json.loads(raw_json)
            for row in obj:
                self.cur.execute("INSERT INTO company VALUES (%s, %s)", (int(row['company_id']), row['company_name']))
            self.conn.commit()
        # self.cur.execute("SELECT * FROM company")
        # self.cur.close()
        # self.conn.close()

    def create_table_vacancy(self):
        self.cur.execute("CREATE TABLE vacancy (vacancy_id int PRIMARY KEY, "
                         "vacancy_name varchar(200) NOT NULL, salary_from int, "
                         "salary_to int, url_vacancy varchar(1000) NOT NULL, "
                         "company_id int NOT NULL)")


        self.conn.commit()
        with open(os.path.join(root_path, self.json_vacancy), 'r', encoding='utf-8') as r_file:
            raw_json = r_file.read()
            obj = json.loads(raw_json)
            for row in obj:
                self.cur.execute("INSERT INTO vacancy VALUES (%s, %s, %s, %s, %s, %s)",
                                 (int(row['vacancy_id']), row['vacancy_name'],
                                  row['salary_from'], row['salary_to'], row['url_vacancy'], int(row['company_id'])))
            self.conn.commit()
        self.cur.execute("SELECT * FROM vacancy")



a = DBManager('companies.json', 'vacancy.json')
a.create_table_companies()
a.create_table_vacancy()






        # cursor.execute(create_table_query)
        #
        # conn.commit()
        # cursor.close()
        # logging.info("Таблица 'vacancies' успешно создана.")

# conn = psycopg2.connect(host='localhost', database='hh_base', user='postgres', password='2162')
# cur =  conn.cursor()
# cur.execute ("CREATE TABLE company (company_id int PRIMARY KEY, company_name varchar(100) NOT NULL)")
# conn.commit()
# cur.close()