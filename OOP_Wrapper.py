class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"\nPerson created with name: {self.name} and age: {self.age}.")

    def display(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id=None, salary=0.0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = float(salary)
        if employee_id is not None:
            print(f"Employee created with name: {name}, age: {age}, "
                  f"ID: {employee_id}, and salary: ${self.__salary}.")

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary < 0:
            print("Salary can't be negative.")
        else:
            self.__salary = float(salary)

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary: $" + str(self.__salary))

    def __del__(self):
        pass

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age)
        self.set_employee_id(employee_id)
        self.set_salary(salary)
        self.department = department
        print(f"Manager created with name: {name}, age: {age}, ID: {employee_id}, "
              f"salary: ${self.get_salary()}, and department: {department}.")

    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $" + str(self.get_salary()))
        print("Department:", self.department)

class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age)
        self.set_employee_id(employee_id)
        self.set_salary(salary)
        self.programming_language = programming_language

    def display(self):
        print("\nDeveloper Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $" + str(self.get_salary()))
        print("Programming Language:", self.programming_language)

def show_menu():
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

def main():
    person = None
    employee = None
    manager = None

    print("--- Python OOP Project: Employee Management System ---")

    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            person = Person(name, age)

        elif choice == "2":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            employee = Employee(name, age, emp_id, salary)

        elif choice == "3":
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            manager = Manager(name, age, emp_id, salary, dept)

            if issubclass(Manager, Employee):
                pass

        elif choice == "4":
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            sub = input("Enter your choice: ")

            if sub == "1":
                if person:
                    person.display()
                else:
                    print("\nNo person created yet.")
            elif sub == "2":
                if employee:
                    employee.display()
                else:
                    print("\nNo employee created yet.")
            elif sub == "3":
                if manager:
                    manager.display()
                else:
                    print("\nNo manager created yet.")
            else:
                print("\nInvalid choice.")

        elif choice == "5":
            print("\nExiting the system.")
            break

        else:
            print("\nInvalid choice, try again.")
            continue

        print("\n--- Choose another operation ---")


if __name__ == "__main__":
    main()
