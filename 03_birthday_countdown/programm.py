import datetime

def print_header():
    print('-----------------------------------------')
    print('        BIRTHDAY COUNTDOWN')
    print('-----------------------------------------')


def get_birthday_from_user():
    year=int(input('Enter Year of Birth [YYYY]:'))
    month = int(input('Enter Month of Birth [MM]:'))
    day = int(input('Enter Day of Birth [DD]:'))

    birthday=datetime.datetime(year,month,day)

    return birthday


def compute_days_difference(birthday, now):
    birthday_this_year=datetime.datetime(now.year, birthday.month, birthday.day)
    td=now - birthday_this_year
    days_diff=int(td.total_seconds() / 60 /60 / 24)
    return days_diff

def print_message(days_diff):
    if days_diff < 0:
        print('Your birthday is in {} days this year'.format(-days_diff))
    elif days_diff > 0:
        print('Your birthday was already {} days ago this year'.format(days_diff))
    else:
        print('Happy Birthday!!')


def main():
    print_header()
    bday=get_birthday_from_user()
    now=datetime.datetime.now()
    dt=compute_days_difference(bday, now)
    print_message(dt)

main()

