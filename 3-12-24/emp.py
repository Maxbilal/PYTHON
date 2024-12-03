class Employee:
    def __init__(self, name, position, base_salary):
        self.name = name
        self.position = position
        self.base_salary = base_salary

    def calculate_annual_salary(self, bonus=0):
        return self.base_salary * 12 + bonus

    def display(self, bonus=0):
        print("Employee:",self.name, "Position = ",self.position)
        print("Base Salary =",self.base_salary, "Annual Salary=" ,self.calculate_annual_salary(bonus))

name = input("Enter the employee's name: ")
position = input("Enter the employee's position: ")
base_salary = float(input("Enter the base salary: "))
bonus = float(input("Enter the annual bonus (if any): "))
employee = Employee(name, position, base_salary)
employee.display(bonus)
