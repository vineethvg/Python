class person(object):

    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name

    def isEmp(self):
        return False


class Employee(person):

    def isEmp(self):
        return True


emp = person("man1")
print(emp.get_name(), emp.isEmp())

emp = Employee("man2")
print(emp.get_name(), emp.isEmp())
