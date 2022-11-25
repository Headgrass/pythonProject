
def search_by_major(major):
    with open("bd_emloyees.txt", 'r') as fo:
        for i in range(fo[major]):
            if i == major:
                to_object = []
        return to_object


def search_by_bd(start_date, end_date):
    with open("bd_emloyees.txt", 'r') as fo:
        for i in range(fo[birthday]):
            if start_date < i > end_date:
                to_object = []
        return to_object


def search_by_salary(start_salary, end_salary):
    with open("bd_emloyees.txt", 'r') as fo:
        for i in range(fo[salary]):
            if start_salary < i > end_salary:
                to_object = []
        return to_object