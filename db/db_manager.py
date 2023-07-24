import psycopg2
from psycopg2._psycopg import cursor

from db.db_abc_class import Abc_dbmanager
from psycopg2.extensions import AsIs


class Dbmanager(Abc_dbmanager):
    def __init__(self, host, database, user, password):
        self.conn = psycopg2.connect(host=host,
                                     database=database,
                                     user=user,
                                     password=password)

    def get_companies_and_vacancies_count(self):
        with self.conn.cursor() as cur:
            cur.execute("select company_name, vacancy_count from company")
            return cur.fetchall()

    def get_all_vacancies(self):
        with self.conn.cursor() as cur:
            cur.execute("select company.company_name, vacancy_name, salary_min, salary_max, url from vacancy "
                        "inner join company using(company_id)")
            return [print(i) for i in cur.fetchall()]

    def get_avg_salary(self):
        with self.conn.cursor() as cur:
            cur.execute("select ROUND(AVG(salary_min), 2) from vacancy where salary_min is not null")
            return cur.fetchall()

    def get_vacancies_with_higher_salary(self):
        with self.conn.cursor() as cur:
            cur.execute("select vacancy_name, url from vacancy where (select avg(salary_min) from vacancy) < salary_min")
            return cur.fetchall()

    def get_vacancies_with_keyword(self):
        with self.conn.cursor() as cur:
            keyword = input("Введите ключевое слово: ")
            cur.execute(f"SELECT vacancy_name, url from vacancy where vacancy_name like '%{keyword}%'")
            return cur.fetchall()
