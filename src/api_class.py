import os

import requests

from abc_class import ApiAbc


class HeadHunterAPI(ApiAbc):
    """Класс для работы с API HeadHunter"""

    def __init__(self, data: str):
        """Инициализатор класса"""
        self.data = data
        self.request = self.get_vacancies()

    def get_vacancies(self):
        """Возвращает вакансии с сайта HeadHunter"""
        try:
            vacancies = []
            for page in range(1, 11):
                params = {
                    "text": f"{self.data}",
                    "area": 113,
                    "page": page,
                    "per_page": 100,
                }
                vacancies.extend(requests.get('https://api.hh.ru/vacancies', params=params).json()["items"])
            return vacancies
        except requests.exceptions.ConnectTimeout:
            print('Connection timeout occurred!')
        except requests.exceptions.ReadTimeout:
            print('Read timeout occurred')
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed..')
        except requests.exceptions.HTTPError as err:
            print('HTTP Error occurred')
            print('Response is: {content}'.format(content=err.response.content))


class SuperJob(ApiAbc):
    """Возвращает вакансии с сайта SuperJob"""

    def __init__(self, data: str):
        """Инициализатор класса"""
        self.data = data
        self.request = self.get_request()

    def get_request(self):
        """Возвращает вакансии с сайта SuperJob"""
        url = "https://api.superjob.ru/2.0/vacancies/"
        params = {'keyword': self.data, "count": 1000}
        my_auth_data = {"X-Api-App-Id": os.environ['SJ_API_KEY']}
        response = requests.get(url, headers=my_auth_data, params=params)
        vacancies = response.json()['objects']
        return vacancies
