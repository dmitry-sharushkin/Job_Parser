from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API сайтов."""
    @abstractmethod
    def get_vacancies(self, search_query):
        """Абстрактный метод для получения списка вакансий с сайта."""
        pass
