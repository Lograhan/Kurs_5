import csv
import json
from data.full_vac import Vacancy
from data.file_manager import File_manager


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


def all_vacancy() -> list:
    """
    Функция для формирования единого списка всех вакансий.
    Возвращает список в котором указаны вакансии с обоих сайтов.
    """
    all_vac = []
    data_hh = File_manager.open_file('save_file/hh.ru.json')
    for vacancy in data_hh:
        vac = Vacancy(vacancy['name'], vacancy['alternate_url'], vacancy['salary']['from'])
        all_vac.append(vac)

    data_sj = File_manager.open_file('save_file/sj.ru.json')
    for i in data_sj:
        vac = Vacancy(i['profession'], i['link'], i['payment_from'])
        all_vac.append(vac)

    return all_vac


def create_file_csv():
    """
    Функция для создания файла .csv
    Наполнение файла ведется в три столбца.
    """
    for vacancy in sorted(all_vacancy(), reverse=True):
        with open('save_file/all_vacancy.csv', 'a', encoding='utf-8') as file:
            data = csv.writer(file)
            data.writerow((vacancy.name, vacancy.url, vacancy.zp))


def clear_file_csv():
    """
    Функция для очистки файла .csv
    После применения в файле остаются только наименования столбцов "Вакансия", "Ссылка на вакансию", "Указанная зарплата".
    """
    with open('save_file/all_vacancy.csv', 'w', encoding='utf-8') as file:
        data = csv.writer(file)
        data.writerow(
            ["Вакансия",
             "Ссылка на вакансию",
             "Указанная зарплата"
             ]
        )


def print_top_vac(n=None) -> list:
    """
    Функция для вывода в терминал определённого количества вакансий.
    Данные берутся в отсортированном виде из полного списка вакансий с двух сайтов.
    В атрибут передается количество желаемых вакансий, по умолчанию значение отсутствует.
    Возвращает список
    """
    sort_vac = sorted(all_vacancy(), reverse=True)
    return [print(i) for i in sort_vac[:n]]


