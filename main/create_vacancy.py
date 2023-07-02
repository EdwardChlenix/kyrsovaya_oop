class Vacancy:
    vacancies_dict = []

    def __init__(self, vacancy_id, title, link, salary_min, salary_max, description):
        self.id = vacancy_id
        self.title = title
        self. link = link
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.description = description

        Vacancy.vacancies_dict.append(self)

    def __str__(self):
        return f"ID: {self.id}\nОписание вакансии: {self.description}"


