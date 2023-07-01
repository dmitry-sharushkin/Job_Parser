from abc import ABC, abstractmethod


class ApiAbc(ABC):
    """Абстрактный класс для оаботы с API"""
    @abstractmethod
    def get_vacancies(self):
        """Абстрактный метод для получения списка вакансий"""
        pass
