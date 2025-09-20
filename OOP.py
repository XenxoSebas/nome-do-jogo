class Employee:

    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Xenxo', 'Sebas', 100)
emp_2 = Employee('Test', 'User', 200)

print(Employee.number_of_employees)

'''emp_1.raise_amount = 1.2

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
'''

'''emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.raise_amount)'''

'''print(emp_1.email)
print(emp_2.email)'''

'''emp_1.fullname()
print(Employee.fullname(emp_1))'''

'''emp_1.first = 'Xenxo'
emp_1.last = 'Sebas'
emp_1.email = 'Xsebas@company.com'
emp_1.pay = 100

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = ('Test.User@company.com')
emp_2.pay = 200

print(emp_1.email)
print(emp_2.email)'''