import json


class JSONSaver:
    """Класс для сохранения вакансий в формате JSON."""

    def save_in_file(self, headhunter=None, superjob=None):
        """Сохраняет вакансии в формате JSON в файл."""
        if headhunter is not None and superjob is None:
            with open('vacancies.json', 'w', encoding='utf-8') as file:
                json.dump(
                    sorted([vars(vacancy) for vacancy in headhunter], key=lambda x: x['salary']['from'], reverse=True),
                    file,
                    ensure_ascii=False,
                    indent=4
                )

        if headhunter is None and superjob is not None:
            with open('vacancies.json', 'w', encoding='utf-8') as file:
                json.dump(
                    sorted([vars(vacancy) for vacancy in superjob], key=lambda x: x['salary']['from'], reverse=True),
                    file,
                    ensure_ascii=False,
                    indent=4
                )

    def get_vacancies_by_salary(self, salary_input):
        """Возвращает вакансии с подходящей зп."""
        with open('vacancies.json', 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
        sorted_dict = []
        try:
            salary, currency = salary_input.split(' ')

        except:
            salary = salary_input
            currency = ['руб', 'rur', 'rub', 'RUR']

        if currency in ['руб', 'RUR', 'rub']:
            currency = ['руб', 'rur', 'rub', 'RUR']

        for vacancy in vacancies:
            try:
                if int(vacancy['salary']['from']) >= int(salary) and vacancy['salary']['currency'] in currency:
                    sorted_dict.append(vacancy)
                elif vacancy['salary']['currency'] in ['usd', 'USD'] and int(vacancy['salary']['from']) * 80 >= int(
                        salary):
                    sorted_dict.append(vacancy)
                elif vacancy['salary']['currency'] in ['eur', 'EUR'] and int(vacancy['salary']['from']) * 90 >= int(
                        salary):
                    sorted_dict.append(vacancy)
            except:
                continue

        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(sorted_dict, file, ensure_ascii=False, indent=4)

    def search_words(self, search_words):
        """Возвращает вакансии, содержащие в описании заданные слова."""
        if not isinstance(search_words, str):
            return "Error: запрос должен быть строкой"
        if search_words == '':
            with open('vacancies.json', 'r', encoding='utf-8') as file:
                vacancies = json.load(file)
            return vacancies
        else:
            with open('vacancies.json', 'r', encoding='utf-8') as file:
                vacancies = json.load(file)
            result = []
            for vacancy in vacancies:
                for word in search_words.split():
                    if vacancy['description'] is not None and search_words in vacancy['description'].lower():
                        result.append(vacancy)
                        break
            return result

    def json_results(self):
        """Возвращает список вакансий, сохраненных в формате JSON."""
        with open('vacancies.json', 'r', encoding='utf-8') as file:
            final_result = json.load(file)
        return final_result
