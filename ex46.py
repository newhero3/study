class Employee:
    raise_amount=1.3
    num_of_employees=0
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+'.'+last+"@company.com"
        self.pay=pay
        
        Employee.num_of_employees+=1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay* self.raise_amount)

class Developer(Employee):
    
    rais_amount=1.10
    
    def __init__(self,first,last,pay):
        super().__init__(first,last,pay)
        
    
dev_1=Developer("John", "Travolta", 50000)
dev_2=Developer('Test', 'Employee', 60000)

# print(emp_1.fullname())
# emp_1.apply_raise()
# print(emp_1.pay)
# emp_1.apply_raise()
# emp_1.apply_raise()
# print(emp_1.pay)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)