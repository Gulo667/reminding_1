class Employee:
    raise_amt=1.40
    def __init__(self, first, last, salary):
        self.first=first
        self.last=last
        self.salary=salary
        self.email = first + "." + last + "@gmail.com"
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.salary=self.salary*self.raise_amt

class Developer(Employee):
    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang
    raise_amt=1.10

class Manager(Employee):
    def __init__(self, first, last, salary, employees=0):
        super().__init__(first, last, salary)
        if employees==0:
            self.employees = []
        else:
            self.employees=employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print("--->", emp.fullname())

    def find_by_email(self, emp_email):
        for emp in self.employees:
            if emp_email==emp.email:
                return emp.fullname()

class Intern(Employee):
    def __init__(self, first, last, salary, school):
        super().__init__(first, last, salary)
        self.school = school
    raise_amt=1.02


dev_1=Developer('sam', 'smith', 5000, 'Python')
dev_2=Developer('dylan', 'brien', 3000, 'java')
#print(f"dev: {dev_1.fullname()}, email: {dev_1.email}, salary: {dev_1.salary}")
dev_1.apply_raise()
#print(f"{dev_1.fullname()}'s new salary is {dev_1.salary}")
mng_1=Manager('susana', 'test', 10000, [dev_1])
mng_1.add_emp(dev_2)

print(mng_1.find_by_email(dev_1.email))