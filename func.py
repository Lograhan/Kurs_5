def add_to_db_comp(database, data) -> None:
    """
    Функция для заполнения таблицы 'company' в БД
    :param database: объект класса Dbmanager()
    :param data: объект класса HH_api()
    """
    with database.conn.cursor() as cur:
        for i in data['items']:
            cur.execute("INSERT INTO company (company_id, company_name, vacancy_count)"
                        "VALUES (%s, %s, %s);",
                        (i['id'],
                         i['name'],
                         i['open_vacancies']))
            database.conn.commit()


def add_to_db_vacancy(database, data) -> None:
    """
    Функция для заполнения таблицы 'vacancy' в БД
    :param database: объект класса Dbmanager()
    :param data: объект класса HH_api()
    """
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


def delete_data_table(database) -> None:
    """
    Функция для удаления данных с таблиц в БД
    :param database: объект класса Dbmanager()
    """
    with database.conn.cursor() as cur:
        cur.execute('delete from vacancy;'
                    'delete from company')
        database.conn.commit()

