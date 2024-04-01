from src.company_file import Apicopmany
from src.vacancy_file import Apivacancy
from src.saver_json import SaveJson
from src.sql_class import DBManager

hh_id = [675794, 562530, 3148, 1276, 1552384, 78638, 1346,  23435, 4934, 20986]
json_company = 'companies.json'
json_vacancy = 'vacancy.json'
hh_companies = Apicopmany()
hh_vacancies = Apivacancy()
company_to_json = SaveJson(json_company)
vacancy_to_json = SaveJson(json_vacancy)
sql_get = DBManager(json_company, json_vacancy)

def user_interaction():
    error_action = str()
    company_list = list()
    vacancy_list = list()
    for id in hh_id:
        api_get_company = hh_companies.get_industry(id)
        company_list.append(api_get_company)
        api_get_vacancy = hh_vacancies.get_vacancyes_company(id)
        for vacancy in api_get_vacancy:
            vacancy_list.append(vacancy)

    company_to_json.add_file_to_json(company_list)
    vacancy_to_json.add_file_to_json(vacancy_list)
    sql_get.create_table_companies()
    sql_get.create_table_vacancy()

    print("\nЗдраствуйте")
    while True:
        Enter_select = input("\nВыберите действие:\n"
                             "1. Вывести все компании и количество их вакансий\n"
                             "2. Вывести все вансии с указанием названия компании, названия вакансии\n"
                             "   и зарплаты и ссылки на вакансию\n"
                             "3. Вывести среднюю зарплату по всем вакансиям\n"
                             "4. Вывести все вакансии, у которых зарплата выше средней по всем вакансиям\n"
                             "5. Вывести все вакансии по ключевому слову\n")
        сhoosing_action(Enter_select)
        further_action = input('\n\nЕсли желаете остановится - введите команду "N",\n'
                               'либо введите любую команду для продолжения\n')
        if further_action != "N":
            continue
        elif further_action == "N":
            repeat_command = input("Будет произведено удаление данных из базы SQL,\n"
                                   "подтверждаете опервцию 'Y'\n"
                                   "либо введите любую команду для продолжения?")
            if repeat_command == "Y":
                sql_get.delete_table()
                print("\nСпасибо, что воспользовались нашими услугами")
                break
            elif repeat_command != "Y":
                continue

def сhoosing_action(number):
    if int(number) == 1:
        sql_get.get_companies_and_vacancies_count()
    elif int(number) == 2:
        sql_get.get_all_vacancies()
    elif int(number) == 3:
        print(DBManager.get_avg_salary(sql_get))
    elif int(number) == 4:
        sql_get.get_vacancies_with_higher_salary(sql_get)
    elif int(number) == 5:
        key_word = input("Введите пожалуйста ключевое слово\n")
        sql_get.get_vacancies_with_keyword(key_word)
    else:
        print("Неверный выбор действия")





