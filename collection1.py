courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

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


def fill_list(people):
    all_list = []
    for name in people:
        all_list.extend(name)
    return all_list


def first_names_list(people):
    all_names_list = []
    for mentor in fill_list(people):
        name = mentor.split()[0]
        all_names_list.append(name)
    return all_names_list


def count_popular_names(names_list):
    unique_names = set(names_list)
    popular = []
    for name in unique_names:
        popular.append([name, names_list.count(name)])  # Добавьте подсчёт имён
    return popular


def most_popular_names(popular, amount):
    popular.sort(key=lambda x: x[1], reverse=True)
    top = popular[:amount]
    top_dict = {}
    for name, count in top:
        top_dict[name] = count
    print(top_dict)
    return top_dict


most_popular_names(count_popular_names(first_names_list(mentors)),5)