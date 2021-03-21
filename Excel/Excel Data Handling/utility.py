# generate employees - 
from emp_classes import Employee, Address

import random

area_list = ["Karve Nagar", "Wakad", "Kothrud", "Katraj", "Bibwwadi", "Aundh", "Baner"]

def generate_address(no):
    address_list = []
    for i in range(no):
        adr = Address(pin=random.randint(411057, 465784), area=random.choice(area_list))
        address_list.append(adr)
    return address_list

adr_list = generate_address(15)
# print(resp)
# print(len(resp))

def generate_name():
    name = '' 
    for i in range(random.randint(4, 8)):   # 4   
        name += chr(random.randint(65, 90))
    return name.title()


# print(generate_name())

def generate_emps(no):
    emp_list = []
    for n in range(1, no+1):  # 0-49
        emp = Employee(eid=100+n, 
                 ename=generate_name(),
                 eage=random.randint(21, 35), 
                 esalary=random.randint(15000, 80000), 
                 eadr=random.choice(adr_list))        
        emp_list.append(emp)
    return emp_list

# generate_emps(50)
# print(emp_list)
# c = 0
# for emp in emp_list:
    # if emp.EmpSalary > 50000:
        # print(emp)
        # c+=1
    # if emp.EmpAddress.Area == 'Aundh':
    #     print(emp)
    #     c += 1
    # print(type(emp))
# print(c)





# using lamda filter, 