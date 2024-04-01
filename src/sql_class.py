import psycopg2
from config import root_path
import os
import json

class DBManager:
    """
    Класса работает с бозой postgresql
    """

    def __init__(self, json_company, json_vacancy):
        self.json_company = json_company
        self.json_vacancy = json_vacancy
        self.conn = psycopg2.connect(host='localhost',
                                         database='hh_base',
                                         user='postgres',
                                         password='2162')
        self.cur =  self.conn.cursor()
    def create_table_companies(self):
        """
        Метод класса, который создает таблицу company в postgresql и заполняет с json файла
        """

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

    def create_table_vacancy(self):
        """
        Метод класса, который создает таблицу vacancy в postgresql и заполняет с json файла
        """
        self.cur.execute("CREATE TABLE vacancy (vacancy_id int PRIMARY KEY, "
                         "vacancy_name varchar(200) NOT NULL, salary_from int, "
                         "salary_to int, url_vacancy varchar(1000) NOT NULL, "
                         "company_id int NOT NULL)")
        with open(os.path.join(root_path, self.json_vacancy), 'r', encoding='utf-8') as r_file:
            raw_json = r_file.read()
            obj = json.loads(raw_json)
            for row in obj:
                self.cur.execute("INSERT INTO vacancy VALUES (%s, %s, %s, %s, %s, %s)",
                                 (int(row['vacancy_id']), row['vacancy_name'],
                                  row['salary_from'], row['salary_to'], row['url_vacancy'], int(row['company_id'])))
            self.conn.commit()
        self.cur.execute("SELECT * FROM vacancy")

    def get_companies_and_vacancies_count(self):
        """
         Метод класса, который вызывает список всех компаний и количество вакансий у каждой компании
        """

        self.cur.execute("SELECT company_id, company_name, COUNT(vacancy.vacancy_id) FROM company "
                         "INNER JOIN vacancy USING (company_id)"
                         "GROUP BY company_id")
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def get_all_vacancies(self):
        """
        Метод класса, который вызывает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """

        self.cur.execute("SELECT company.company_name, vacancy.vacancy_name, vacancy.salary_from, "
                         "vacancy.salary_to, vacancy.url_vacancy FROM company INNER JOIN vacancy USING(company_id)")
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
    @staticmethod
    def get_avg_salary(ex_cls):
        """
        Метод класса, который получает среднюю зарплату по вакансиям
        """
        count = 0
        ex_cls.cur.execute("SELECT salary_from, salary_to FROM vacancy "
                         "WHERE salary_from IS NOT  NULL and salary_to IS NOT NULL")
        ex_cls.conn.commit()
        rows = ex_cls.cur.fetchall()
        for row in rows:
            if row[0] == 0:
                count += row[1]
            elif row[1] == 0:
                count += row[0]
            else:
                count += (row[0] + row[1]) / len(row)

        return (int(count / len(rows)))

    def get_vacancies_with_higher_salary(self, ex_cls):
        """
        Метод класса, который вызывает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        avg_salary = DBManager.get_avg_salary(ex_cls)
        self.cur.execute("SELECT * FROM vacancy "
                    "WHERE salary_from IS NOT  NULL and salary_to IS NOT NULL")
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows:
            if row[2] == 0 and row[3] > avg_salary:
                print(row)
            elif row[3] == 0 and row[2] > avg_salary:
                print(row)
            elif (row[2] + row[3]) / 2 > avg_salary:
                print(row)

    def get_vacancies_with_keyword(self, user_word):
        """
        Метод класса, который вызывает список всех вакансий, в названии которых содержатся
        переданные в метод слова, например python.
        """
        word = list()
        self.cur.execute("SELECT * FROM vacancy")
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows:
            if user_word.lower() in row[1].lower():
                word.append(row)
        if len(word) == 0:
            print('Вакансим по ключевому слову не найдены')
        elif len(word) != 0:
            for temp in word:
                print(temp)

    def delete_table(self):
        """
        Метод класса - завершающий, он удаляет таблицы и закрывает cur и conn
        """
        self.cur.execute("DROP TABLE vacancy")
        self.cur.execute("DROP TABLE company")
        self.conn.commit()
        self.cur.close()
        self.conn.close()