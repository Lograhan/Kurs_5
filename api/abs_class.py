from abc import ABC, abstractmethod


class Api(ABC):

    @abstractmethod
    def get_api_comp(self):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass
