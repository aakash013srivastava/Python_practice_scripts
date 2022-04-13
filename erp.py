
#  Script for employee management system

import os

org = {'dept':['tech','accounts','hr','mgmt'],
        'designations':{'tech':['dev','lead','arch'],
                        'accounts':'manager',
                        'hr':['recruiter','Head'],
                        'mgmt':['pm','senior pm']}}

if os.path.exists('erp.csv') and os.stat('erp.csv').st_size != 0:
    f= open('erp.csv','r')
    employees = f.readlines()
    f.close()
else:
    f = open('erp.csv','w')
    employees=[]
    f.close()


def create_employee():
    emp = input("Enter name of the employee:")
    dept = input("Enter the department:")
    designation = input("Enter the designation:")
    if dept in org['dept'] and designation in org['designations'][dept]:
        f= open('erp.csv','a')
        f.write(emp+","+dept+","+designation+"\n")
        f.close()
        
    else:
        print("No such department/designation exists\n")

def print_employees():
    for line in employees:
        print(line)

def edit_employees():
    emp = input("Enter name of the employee:")
    dept = input("Enter the department:")
    designation = input("Enter the designation:")
    print(employees)
    string = emp+","+dept+","+designation+"\n"
    index = employees.index(string)
    
    for line in employees:
        
        if string == line:
            
            print("Enter new Details:")
            emp2 = input("Enter name of the employee:")
            dept2 = input("Enter the department:")
            designation2 = input("Enter the designation:")
            string2 = emp2+","+dept2+","+designation2+"\n"
            employees[index] = string2
            
            if dept in org['dept'] and designation in org['designations'][dept]:
                f= open('erp.csv','w')
                f.writelines(employees)
                f.close()
        
            else:
                print("No such department/designation exists\n")
            
            print("Employee edited !!!")
            break
        else:
            print("No Such employee")
            



while(True):
    choice = int(input("Enter 1:Create Employee 2:Print Employees 3:Edit Employees 4:Exit\n"))
    if choice == 1:
        create_employee()
        
    elif choice == 2:
        print_employees()
    
    elif choice == 3:
        edit_employees()

    elif choice == 4:
        print("Goodbye!!!")
        break
    else:
        print("Choose again!!!")
        continue
