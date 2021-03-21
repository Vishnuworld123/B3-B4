


# Hierarchical

class Common:
    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)

class Employee(Common):
    """for employee details"""
    def __init__(self, eid, ename, eage, esalary, eadr):
        self.EmpID = eid 
        self.EmpName = ename
        self.EmpAge = eage
        self.EmpSalary = esalary
        self.EmpAddress = eadr

class Address(Common):
    """for employee's address"""
    def __init__(self, pin, area, city="Pune"):
        self.Pincode = pin
        self.Area = area
        self.City = city


if __name__ == "__main__":
    a1 = Address(pin=431820,area="Wakad", city="Pune")
    print(a1)
    e1 = Employee(eid=101, ename="ABC", eage=25, esalary=45415, eadr=a1)
    print(e1)