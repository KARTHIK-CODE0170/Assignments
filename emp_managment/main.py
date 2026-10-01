from employee import Employee
def main():
    print(f"Comapany :",Employee.COMPANY_NAME)
    print('Employees before:',Employee.total_employees)
    e1 = Employee(name="Ravi Kumar",emp_id=101,department="Engineering",salary=60000,pan_number='12x545')
    e2 = Employee(name="Anita Sharma",emp_id=102,department="Finance",salary=75000,pan_number='11x445')
    print(e1,e2,sep="\n")
    print("Employees after:",Employee.total_employees)
    print('PF for e1:',e1.calculate_pf())
    print("After 10% hike:",e1.apply_hike(10))
    print(e1.transfer_department("Data Science"))
    print(f"Is valid salary 9000 : {e1.is_valid_salary(9000)}")
    # print(type(e1._department))
    print("protected :",e1._department)
    print("private :",e1._Employee__pan_number)


if __name__ == '__main__':
    main()