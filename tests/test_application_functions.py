from application.salary import calculate_salary
from application.db.people import get_employees


def test_calculate_salary():
    expected_output = 'Hello reviewer! Now the calculate_salary function is runnig!'
    assert calculate_salary() == expected_output


def test_get_employees():
    expected_output = 'And now the get_employees function is runnig too!'
    assert get_employees() == expected_output

