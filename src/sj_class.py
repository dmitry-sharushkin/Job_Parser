import os

import requests

from src.abstract_class import AbstractAPI
from src.vacancy_class import Vacancy


class SuperJobAPI(AbstractAPI):
    """Класс для работы с API SuperJob."""
    __slots__ = ("api_key", "headers", "url")

    def __init__(self):
        """Инициализирует класс"""
        self.api_key = os.getenv('SJ_API_KEY')
        self.headers = {'X-Api-App-Id': self.api_key}
        self.url = "https://api.superjob.ru/2.0/vacancies/"

    def get_vacancies(self, search_query):
        """Получает список вакансий."""
        params = {
            'keyword': search_query,
            'count': 100,
        }

        response = requests.get(self.url, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            vacancies_data = data['objects']
            vacancies = []
            for vacancy in vacancies_data:
                title = vacancy['profession']
                salary = SuperJobAPI.get_salary(vacancy)
                description = vacancy['candidat']
                url = vacancy['link']
                vacancy = Vacancy(title, salary, description, url)
                vacancies.append(vacancy)
            return vacancies
        else:
            return f'Error: {response.status_code}'

    def get_salary(salary_data, **kwargs):
        """Возвращает словарь с информацией о зарплате вакансии."""
        if salary_data.get('payment_to') == 0:
            salary = {'from': salary_data['payment_from'], 'currency': salary_data['currency']}
        elif salary_data.get('payment_from') == 0:
            salary = {'from': salary_data['payment_to'], 'currency': salary_data['currency']}
        else:
            salary = {'from': salary_data.get('payment_from', 0), 'to': salary_data.get('payment_to', 0),
                      'currency': salary_data.get('currency', 'rub')}
        return salary
