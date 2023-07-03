import json
from abc import ABC
import requests
from abstract_class import JobSites
from create_vacancy import Vacancy

class HeadHunter(JobSites, ABC):
    def __init__(self, keyword, vacancies_count):
        self.vacancies_count = vacancies_count
        self.keyword = keyword
        self.min_salary = None

    def server_connection(self, params=None):

        url = 'https://api.hh.ru/vacancies'
        params = {'text': self.keyword, 'per_page': self.vacancies_count}
        headers = {'User-Agent': '322322'}
        response = requests.get(url, params=params, headers=headers)

        return response

    def job_dictionary(self, **kwargs):
        if self.server_connection().status_code == 200:
            data = self.server_connection().json()
            list_of_jobs = []
            for item in data['items']:
                vacancy_id = item['id']
                title = item['name']
                url = item['alternate_url']

                if item['salary']:
                    salary_min = item['salary']['from']
                    salary_max = item['salary']['to']

                else:
                    salary_min = None
                    salary_max = None

                vacancy_description = item['snippet']['requirement']

                job = {
                    'id': vacancy_id,
                    'title': title,
                    'link': url,
                    'salary_min': salary_min,
                    'salary_max': salary_max,
                    'description': vacancy_description
                }
                list_of_jobs.append(job)
            self.file_vacancy(list_of_jobs)
            return list_of_jobs

        else:
            print(f'Не удалось выполнить запрос, код ошибки - {self.server_connection().status_code}')


    def file_vacancy(self, list_of_jobs):
        with open('vacancies.json', 'w', encoding='utf-8') as f:
            json.dump(list_of_jobs, f, ensure_ascii=False)


def hh_function(keyword, vacancies_count):
    first_dict = HeadHunter(keyword, vacancies_count)
    job_dict = first_dict.job_dictionary()
    Vacancy.vacancies_dict = job_dict
    for item in Vacancy.vacancies_dict:
        print(str(item))


