import os
from datetime import datetime, timedelta


path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(path))
eugene_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(eugene_path, 'r', encoding='utf-8') as data_file:
        all_data = []
        for line in data_file:
            i = line.strip()
            all_data.append(i)
        return all_data


def extract_date(str):
    before_dash = str.split(' - ')[0]
    after_dot = before_dash.split('. ')[1]
    return after_dot


def parse_date(str):
    date = datetime.strptime(str, '%Y-%m-%d %H:%M:%S.%f')
    return date


lines = read_file()
str1 = extract_date(lines[0])
str2 = extract_date(lines[1])
str3 = extract_date(lines[2])
date1 = parse_date(str1)
date2 = parse_date(str2)
date3 = parse_date(str3)
now = datetime.now()
date_week = date1 + timedelta(hours=168)
day_of_week = date1.strftime('%A')
number_days = now - date3
print(f"Дата на неделю позже: {date_week}")
print(f"День недели: {day_of_week}")
print(f"Сколько дней назад: {number_days.days}")
