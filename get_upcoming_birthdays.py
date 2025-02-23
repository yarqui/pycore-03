import datetime as dt

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.02.23"}
]


def get_upcoming_birthdays(users: list) -> list:
    to_greet = []
    today = dt.date.today()
    print('today', today)
    week_ahead = today + dt.timedelta(days=7)

    for user in users:
        birth_date = dt.datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday_this_year = birth_date.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= week_ahead:
            print(birthday_this_year)
            if birthday_this_year.weekday() in (5,6): # weekends
                birthday_this_year += dt.timedelta(days=(7 - birthday_this_year.weekday()))
        
            to_greet.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')
            })
    
    return to_greet

upcoming_birthdays = get_upcoming_birthdays(users)
print("Birthday bash for this week:", upcoming_birthdays)