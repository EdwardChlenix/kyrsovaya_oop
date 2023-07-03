from headhunter import hh_function
from superjob import sj_function

def user_interaction():

    print('Здравствуйте, давайте найдем для вас работу')

    job_platform = input("Выберите платформу поиска работы \n1 - HeadHunter \n2 - SuperJob\n")
    keyword = input("Введите ключевое слово для поиска\n")
    vacancies_count = input("Какое количество вакансий показать?\n")
    city_for_search = input("В каком городе вакансии вас интересуют?\n")

    keyword_final = keyword + ' ' + city_for_search

    if job_platform == "1":
        hh_function(keyword_final, vacancies_count)

    elif job_platform == "2":
        sj_function(keyword_final, vacancies_count)


if __name__ == '__main__':
    user_interaction()