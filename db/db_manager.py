import psycopg2
from db_abc_class import Abc_dbmanager


class Dbmanager(Abc_dbmanager):
    def __init__(self, host, database, user, password):
        self.conn = psycopg2.connect(host=host,
                                     database=database,
                                     user=user,
                                     password=password)

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
                            (i['items'][0]['id'],
                             i['items'][0]['name'],
                             i['items'][0]['employer']['id'],
                             i['items'][0]['salary']['from'],
                             i['items'][0]['salary']['to'],
                             i['items'][0]['alternate_url'],))
                database.conn.commit()

    def get_companies_and_vacancies_count(self):
        with self.conn.cursor() as cur:
            cur.execute("select company_name, vacancy_count from company")
            return cur.fetchall()

    def get_all_vacancies(self):
        with self.conn.cursor() as cur:
            cur.execute("select company.company_name, vacancy_name, salary_min, salary_max, url from vacancy "
                        "inner join company using(company_id)")
            return cur.fetchall()

    def get_avg_salary(self):
        with self.conn.cursor() as cur:
            cur.execute("")
            return cur.fetchall()



