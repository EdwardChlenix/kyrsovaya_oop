import json
from abc import ABC
import requests
from abstract_class import JobSites

class HeadHunter(JobSites, ABC):
    def __init__(self, keyword, vacancies_count):
        self.vacanies_count = vacancies_count
        self.keyword = keyword
        self.min_salary = None

    def server_connection(self, params=None):

        url = 'https://api.hh.ru/vacancies'
        params = {'text': self.keyword, 'per page': self.vacanies_count}
        headers = {'User-Agent': '322322'}
        response = requests.get(url, params=params, headers=headers)

        return response

    def job_dictionary(self, **kwargs):
        if self.server_connection().status_code == 200:
            data = self.server_connection().json()
            list_of_jobs = []
            for item in data['items']:
                vacancie_id = item['id']
                title = item['name']
                url = item['alternate_url']

                if item['salary']:

