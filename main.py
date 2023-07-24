from dotenv import load_dotenv
from db.db_manager import Dbmanager
from api.class_hh import HH_api
from func import add_to_db_comp, add_to_db_vacancy, delete_data_table
import os
from api.class_hh import printj
import text_

if __name__ == '__main__':
    load_dotenv()

    database = Dbmanager(
        host='localhost',
        database='postgres',
        user='postgres',
        password=os.environ.get('DB_PASSWORD')
    )

    hh = HH_api()
    company = hh.get_api_comp()
    vacancy = hh.get_vacancy()

    delete_data_table(database, company)
    delete_data_table(database, vacancy)

    add_to_db_comp(database, company)
    add_to_db_vacancy(database, vacancy)

    print(text_.text_1)

    while True:
        user_input_1 = input()
        if user_input_1 == '':
            print(text_.text_2)
            break
        else:
            print('Пожалуйста, нажмите Enter')
            continue

    while True:
        user_input_2 = input('\nВыберите желаемый вариант: \n')
        if user_input_2 == '1':
            printj(database.get_companies_and_vacancies_count())
            continue
        elif user_input_2 == '2':
            print(database.get_all_vacancies())
            continue
        elif user_input_2 == '3':
            print(database.get_avg_salary())
            continue
        elif user_input_2 == '4':
            printj(database.get_vacancies_with_higher_salary())
            continue
        elif user_input_2 == '5':
            print(database.get_vacancies_with_keyword())
            continue
        elif user_input_2 == '6':
            print(text_.text_3)
            break
        else:
            print('Пожалуйста, выберите желаемый вариант: \n')
            continue

