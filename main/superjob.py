import json
import os
from abc import ABC

import requests
from abstract_class import JobSites
from create_vacancy import Vacancy
class SuperJob(JobSites, ABC):

    def __init__(self, keyword, vacancies_count):
        self.vacanies_count = vacancies_count
        self.keyword = keyword
        self.min_salary = None


    def server_connection(self):
        params = {"count": self.vacanies_count, "page": None,
                  "keyword": self.keyword, "archive": False, }
        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': os.getenv('API_KEY'),
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
        return data

    def job_dictionary(self, **kwargs):
        if self.server_connection().status_code == 200:
            data = self.server_connection().json()
            list_of_jobs = []
            for item in data['items']:
                vacancie_id = item['id']
                title = item['name']
                url = item['alternate_url']

                if item['salary']:
                    salary_min = item['salary']['from']
                    salary_max = item['salary']['to']

                else:
                    salary_min = None
                    salary_max = None

                vacancie_description = item['snippet']['requirement']

                jobs = {
                    'id': vacancie_id,
                    'title': title,
                    'link': url,
                    'salary_min': salary_min,
                    'salary_max': salary_max,
                    'description': vacancie_description
                }
                list_of_jobs.append(jobs)
            self.file_vacancy(list_of_jobs)
            return list_of_jobs

        else:
            print(f'Не удалось выполнить запрос, код ошибки - {self.server_connection().status_code}')

    def file_vacancy(self, list_of_jobs):
        with open('vacancies.json', 'w', encoding='utf-8') as f:
            json.dump(list_of_jobs, f, ensure_ascii=False)



def hh_function(keyword, vacancies_count):
    dict = SuperJob(keyword, vacancies_count)
    job_dict = dict.job_dictionary()
    Vacancy.vacancies_dict
    for item in Vacancy.vacancies_dict:
        print(str(item))