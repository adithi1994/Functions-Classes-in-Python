class  Employee_Registration():
    def __init__(self,emp_id,name,age,department,salary):
        self.emp_id=emp_id;
        self.name=name;
        self.age=age;
        self.department=department;
        self.salary=salary;

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary:.2f}")

employee1 = Employee_Registration(120,'Fathima',36,'HR',20000)
employee2 = Employee_Registration(121,'Nehla',32,'IT',25000)
employee3 = Employee_Registration(122,'Firoz',42,'SALES',10000)
employee4 = Employee_Registration(123,'celina',26,'Finance',30000)

employee4.display_info()
