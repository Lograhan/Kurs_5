import json
import requests

from api.abs_class import Api
from hh_api_config import par_comp


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class HH_api(Api):
    """
    Класс для работы с HH.ru
    """

    def __init__(self, page=0) -> None:
        self.par = {
            'page': page,
            'area': par_comp.get('area'),
            'per_page': par_comp.get('per_page'),
            'only_with_vacancies': par_comp.get('only_with_vacancies')
        }

    def get_api_comp(self) -> list[dict]:
        """
        Метод для получения списка компаний.
        Возвращает список в формате json
        """
        data = requests.get('https://api.hh.ru/employers', self.par)
        return data.json()

    def get_vacancy(self):
        """
        Метод для получения списка вакансий, полученный из списка компаний,
        возвращаемых в методе .get_api_comp
        :return: Возвращает список в формате json.
        """
        vacancy = []
        for vac in HH_api.get_api_comp(self)['items']:
            for i in requests.get(vac['vacancies_url']).json()['items']:
                vacancy.append(i)
        return vacancy


