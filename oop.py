class Employee:
    raise_pay = 1.05

    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = name + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}' .format(self.name, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_pay)
        return self.pay

emp_1 = Employee('Olumide', 'Ogundeji', 150000)
emp_2 = Employee('Oluwafemi', 'Ogundeji', 20000)

print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
print(emp_1.fullname())
print(emp_1.pay)
print(emp_1.apply_raise())
print(emp_2.pay)
print(Employee.apply_raise(emp_2))
print(emp_1.email)
print(emp_2.email)
