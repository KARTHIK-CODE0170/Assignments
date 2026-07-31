class Employee:
    #class variables
    total_employees = 0
    COMPANY_NAME = "TechCorp Solutions"
    MIN_SALARY = 15000
    MAX_SALARY = 500000
    pf_percentage = 12.0

    def __init__(self,name='',emp_id=0.0,department='',salary=0.0,pan_number=''):
        self.name = name
        self._emp_id = emp_id
        self._department = department
        self._salary = salary
        self.__pan_number = pan_number
        Employee.total_employees += 1
        
    
    @staticmethod
    def company_name():
        print(Employee.COMPANY_NAME)

#EMP READING
    @property
    def emp_id(self):
        return self._emp_id
    @emp_id.setter
    def emp_id(self,id):
        raise AttributeError("Assigning is not possible for employee id")

    def get_total_employees(cls):
        return cls.total_employees

#DEPARTMENT
    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self,department):
        if isinstance(department,str) and department.isalpha():
            self._department = department
        else:
            raise ValueError("Invalid Department")
    
    def transfer_department(self,dep):
            old_dep = self._department
            new_dep = dep
            self._department = dep
            print(f"{self.name}  moved from {old_dep} to {new_dep}")
            

#SALARY

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,amount):
        if not isinstance(amount,(int, float)):
            raise TypeError("Invalid data")
        elif not (Employee.MIN_SALARY <= amount <= Employee.MAX_SALARY):
            raise ValueError(f"Salary must be in the range of {Employee.MIN_SALARY} and {Employee.MAX_SALARY}" )
        else:
            self._salary = amount
    
    def apply_hike(self,percentage=-1):
        if 0 <= percentage <= 50:
            self._salary += self._salary *(percentage/100)
            return self._salary
        else:
            raise ValueError("Hike percentage is not in the range of 0 and 50")
    
    def calculate_pf(self):
        return self._salary*(Employee.pf_percentage/100)

    @staticmethod
    def is_valid_salary(amount):
        return True if Employee.MIN_SALARY <= amount <= Employee.MAX_SALARY else False
    
    def __str__(self):
        return f"Employee [{self._emp_id}] {self.name} | {self._department} Rs.{self._salary:,.2f}"

    




if __name__ == '__main__':
    # e1 = Employee("Askok",123,'AIml',150,'13ersodvijao')
    # print(e1.__dict__)
    e1 = Employee()
    print(e1)