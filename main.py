from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    print('текущая дата: ', datetime.now())
    print(calculate_salary())
    print(get_employees())