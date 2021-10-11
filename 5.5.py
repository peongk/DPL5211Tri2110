#StudentID: 1201201695
#StudentName: Peong Khay Zhien

def get_bonus(units):
    if(units>500 and units<=1000):
        bonus = salary * 0.1 + salary
    elif(units>1000):
        bonus = salary * 0.2
    else:
        bonus = 0
    return bonus


def get_nett_salary(bonus, salary):
    nettSalary=bonus+salary
    return nettSalary

def display(id, salary, units, bonus, nettSalary):
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("     SALARY SLIP     ")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Staff ID    : {}".format(id))
    print(" Staff salary    : RM{:.2f}".format(salary))
    print(" Units sold    : {}".format(units))
    print(" Bonus    : RM{:.2f}".format(bonus))
    print(" NettSalary    : RM{:.2f}".format(nettSalary))




print("~~~~~~~~~~~~~~~~~~~~~~~")
print("     DATA ENTRY     ")
print("~~~~~~~~~~~~~~~~~~~~~~~")
id = int(input("Enter staff id  : "))
salary = float(input("Enter staff salary    : RM"))
units = int(input("Enter total units sold   :"))
bonus=get_bonus(units)
nettSalary=get_nett_salary(bonus, salary)
display(id, salary, units, bonus, nettSalary)