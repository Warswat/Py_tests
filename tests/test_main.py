import unittest
import pytest


from collection1 import fill_list, first_names_list, most_popular_names, count_popular_names
from collection2 import find_shortest_course, find_longest_course
from collection3 import get_sorted_dict
from yandex_api import check_disk_for_folder, create_folder
from yandex_auth import yandex_auth

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]


class TestMain(unittest.TestCase):
    def test_empty_list(self):
        mentors = [
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
             "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
             "Азамат Искаков", "Роман Гордиенко"],
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
             "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
             "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков",
             "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
             "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
             "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин",
             "Михаил Ларченко"]
        ]
        expected = []
        actual = fill_list(mentors)
        self.assertNotEqual(expected, actual)

    def test_russian_names(self):
        mentors = [
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
             "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
             "Азамат Искаков", "Роман Гордиенко"],
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
             "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
             "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков",
             "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
             "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
             "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин",
             "Михаил Ларченко"]
        ]
        pattern = r"[а-яА-Я]"
        for item in first_names_list(mentors):
            self.assertRegex(item, pattern)


@pytest.mark.parametrize(
        'number,expected',
        (
            [1,1],
            [5,5],
            [3,3],
        )
    )
def test_most_popular(number,expected):
    mentors = [
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
             "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
             "Азамат Искаков", "Роман Гордиенко"],
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
             "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
             "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков",
             "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
             "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
             "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин",
             "Михаил Ларченко"]
    ]
    assert len(most_popular_names(count_popular_names(first_names_list(mentors)),number)) == expected


def test_shortest_course():
    courses = ['Python-разработчик с нуля']
    durations = [14, 20, 12, 20]
    expected = {'Python-разработчик с нуля': 12}
    actual = find_shortest_course(courses,durations)
    assert expected == actual


def test_shortest_course2():
    courses = ['Python-разработчик с нуля']
    durations = [14, 20, 12, 20]
    expected = 12
    actual = find_shortest_course(courses,durations)['Python-разработчик с нуля']
    assert expected == actual


def test_longest_course():
    courses = ['Fullstack-разработчик на Python', 'Frontend-разработчик с нуля']
    durations = [14, 20, 12, 20]
    expected = 20
    actual = find_longest_course(courses, durations)['Fullstack-разработчик на Python']
    actual2 = find_longest_course(courses, durations)['Frontend-разработчик с нуля']
    assert expected == actual
    assert expected == actual2


def test_sorted_course_dict():
    durations_dict = {12: [2], 14: [0], 20: [1, 3]}
    courses_list = [
        {'title': 'Java-разработчик с нуля',
         'mentors': ['Филипп Воронов', 'Анна Юшина', 'Иван Бочаров', 'Анатолий Корсаков', 'Юрий Пеньков', 'Илья Сухачев',
                     'Иван Маркитан', 'Ринат Бибиков', 'Вадим Ерошевичев', 'Тимур Сейсембаев', 'Максим Батырев',
                     'Никита Шумский', 'Алексей Степанов', 'Денис Коротков', 'Антон Глушков', 'Сергей Индюков',
                     'Максим Воронцов', 'Евгений Грязнов', 'Константин Виролайнен', 'Сергей Сердюк',
                     'Павел Дерендяев'],
         'duration': 14},
        {'title': 'Fullstack-разработчик на Python',
         'mentors': ['Евгений Шмаргунов', 'Олег Булыгин', 'Александр Бардин', 'Александр Иванов', 'Кирилл Табельский',
                     'Александр Ульянцев', 'Роман Гордиенко', 'Адилет Асканжоев', 'Александр Шлейко', 'Алена Батицкая',
                     'Денис Ежков', 'Владимир Чебукин', 'Эдгар Нуруллин', 'Евгений Шек', 'Максим Филипенко', 'Елена Никитина'],
         'duration': 20},
        {'title': 'Python-разработчик с нуля',
         'mentors': ['Евгений Шмаргунов', 'Олег Булыгин', 'Дмитрий Демидов', 'Кирилл Табельский', 'Александр Ульянцев',
                     'Александр Бардин', 'Александр Иванов', 'Антон Солонилин', 'Максим Филипенко', 'Елена Никитина',
                     'Азамат Искаков', 'Роман Гордиенко'], 'duration': 12},
        {'title': 'Frontend-разработчик с нуля',
         'mentors': ['Владимир Чебукин', 'Эдгар Нуруллин', 'Евгений Шек', 'Валерий Хаслер', 'Татьяна Тен',
                     'Александр Фитискин', 'Александр Шлейко', 'Алена Батицкая', 'Александр Беспоясов', 'Денис Ежков',
                     'Николай Лопин', 'Михаил Ларченко'],
         'duration': 20}]
    expected = {'Python-разработчик с нуля': 12,
                'Java-разработчик с нуля': 14,
                'Fullstack-разработчик на Python': 20,
                'Frontend-разработчик с нуля': 20}
    actual = get_sorted_dict(durations_dict,courses_list)
    assert expected == actual


def test_yandex_exist_folder():
    headers = {'Authorization': " token "}
    folder_path = "testovichok/"
    expected = range(200, 300)
    actual = check_disk_for_folder(headers,folder_path).status_code
    assert actual in expected


def test_create_folder():
    headers = {'Authorization': " token "}
    folder_path = "testovichok/"
    expected = range(200, 300)
    actual = create_folder(headers, folder_path).status_code
    assert actual in expected


def test_yandex_auth():
    login = ' login '
    password = " password "
    expected = "https://id.yandex.ru/"
    actual = yandex_auth(login,password)
    assert expected == actual


def test_yandex_wrong_login():
    login = ' wrong login '
    password = " password "
    expected = "Wrong login"
    actual = yandex_auth(login,password)
    assert expected == actual


def test_yandex_wrong_password():
    login = ' login '
    password = " wrong password "
    expected = "https://id.yandex.ru/"
    actual = yandex_auth(login, password)
    assert expected != actual
