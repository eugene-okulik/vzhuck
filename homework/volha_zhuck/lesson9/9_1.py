import datetime

my_date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %I:%M:%S')
human_month = python_date.strftime('%B')
new_date = python_date.strftime('%d.%m.%Y, %I:%M')  # Распечатайте дату в таком формате: "15.01.2023, 12:05"
print(human_month)
print(new_date)
