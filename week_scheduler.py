
# Script to schedule upcoming week

days = {0:"",
        1:"",
        2:"",
        3:"",
        4:"",
        5:"",
        6:""}

def schedule_week(days):
    print("Days:\nMonday:0\nTuesday:1\nWednesday:2\nThursday:3\nFriday:4\nSaturday:5\nSunday:6\n")
    inp_day =int(input("Enter Day Number to Schedule:"))
    inp_activities =input("Enter Day Activities to Schedule with space:")
    days[inp_day]+= inp_activities

def print_days_schedule(days):
    inp_day =int(input("Enter Day Number to See Schedule:"))
    print(days[inp_day])

def reset_day(days):
    print("Days:\nMonday:0\nTuesday:1\nWednesday:2\nThursday:3\nFriday:4\nSaturday:5\nSunday:6\n")
    inp_day =int(input("Enter Day Number to Reset:"))
    days[inp_day] = ""

while(True):
    inp = int(input("Enter choice:\n1->Scheduling \n2->Prinitng Schedule\n4->Reset Days Schedule\n3->Exit\n"))
    if inp==1:
        schedule_week(days)
    elif inp ==2:
        print_days_schedule(days)
    elif inp ==3:
        reset_day(days)
    elif inp == 4:
        break
    else:
        print("Wrong choice")
        continue

