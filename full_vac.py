class Vacancy:
    """
    Класс для работы с вакансиями.
    В атрибут принимает Имя вакансии, ссылку на вакансию и ЗП.
    """

    def __init__(self, name, url, zp, ) -> None:
        self.__name = name
        self.__url = url
        self.__zp = zp

    def __str__(self):
        return f'{self.name}, {self.__url}, {self.__zp}'

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        if isinstance(value, str):
            self.__url = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value

    @property
    def zp(self):
        return self.__zp

    @zp.setter
    def zp(self, value):
        if isinstance(value, int):
            self.__zp = value

    def __gt__(self, other):
        return self.__zp > other.__zp
