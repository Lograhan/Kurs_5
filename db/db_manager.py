import psycopg2
from db.db_abc_class import Abc_dbmanager


class Dbmanager(Abc_dbmanager):
    """
    Класс для работы с БД.
    """
    def __init__(self, host, database, user, password) -> None:
        self.conn = psycopg2.connect(host=host,
                                     database=database,
                                     user=user,
                                     password=password)

    def get_companies_and_vacancies_count(self) -> list[dict]:
        """
        Метод для получения списка вакансий и количества вакансий
        """
        with self.conn.cursor() as cur:
            cur.execute("select company_name, vacancy_count from company")
            return cur.fetchall()

    def get_all_vacancies(self) -> list[None]:
        """
        Метод для получения всех вакансий.
        """
        with self.conn.cursor() as cur:
            cur.execute("select company.company_name, vacancy_name, salary_min, salary_max, url from vacancy "
                        "inner join company using(company_id)")
            return [print(i) for i in cur.fetchall()]

    def get_avg_salary(self) -> float:
        """
        Метод для получения среднего значения зарплаты по всем вакансиям
        """
        with self.conn.cursor() as cur:
            cur.execute("select ROUND(AVG(salary_min), 2) from vacancy where salary_min is not null")
            return cur.fetchall()

    def get_vacancies_with_higher_salary(self) -> list[dict]:
        """
        Метод для вывода вакансий, чья зарплата выше средней
        """
        with self.conn.cursor() as cur:
            cur.execute("select vacancy_name, url from vacancy where (select avg(salary_min) from vacancy) < salary_min")
            return cur.fetchall()

    def get_vacancies_with_keyword(self) -> list[dict]:
        """
        Метод для вывода вакансий выбранных по ключевому слову.
        """
        with self.conn.cursor() as cur:
            keyword = input("Введите ключевое слово: ")
            cur.execute(f"SELECT vacancy_name, url from vacancy where vacancy_name like '%{keyword}%'")
            return cur.fetchall()
