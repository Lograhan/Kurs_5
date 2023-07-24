import json

import requests
from api.class_hh import printj


def add_to_db_comp(database, data):
    with database.conn.cursor() as cur:
        for i in data['items']:
            cur.execute("INSERT INTO company (company_id, company_name, vacancy_count)"
                        "VALUES (%s, %s, %s);",
                        (i['id'],
                         i['name'],
                         i['open_vacancies']))
            database.conn.commit()


def add_to_db_vacancy(database, data):
    with database.conn.cursor() as cur:
        for i in data:
            cur.execute("INSERT INTO vacancy (vacancy_id, vacancy_name, company_id, salary_min,"
                        "salary_max, url) VALUES (%s, %s, %s, %s, %s, %s);",
                        (i['id'],
                         i['name'],
                         i['employer']['id'],
                         i['salary']['from'],
                         i['salary']['to'],
                         i['alternate_url'],))
            database.conn.commit()


def delete_data_table(database, data):
    with database.conn.cursor() as cur:
        cur.execute('delete from vacancy;'
                    'delete from company')
        database.conn.commit()

