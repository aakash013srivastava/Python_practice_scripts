
# Script to schedule upcoming week

import json
import os
days = ""
def create_file_structure():
    f = open('schedule.txt','w')
    struct = {'0':"",'1':"",'2':"",'3':"",'4':"",'5':"",'6':""}
    string = json.dumps(struct)
    f.write(string)
    f.close()

if not os.path.exists('schedule.txt'):
    create_file_structure()

if os.stat('schedule.txt').st_size == 0:
    print("file is empty")
    create_file_structure()
else:
    json_file =  open('schedule.txt','r')
    days = json.load(json_file)
    print((days))



    def schedule_week(days):
        print("Days:\nMonday:0\nTuesday:1\nWednesday:2\nThursday:3\nFriday:4\nSaturday:5\nSunday:6\n")
        inp_day =(input("Enter Day Number to Schedule:"))
        inp_activities =input("Enter Day Activities to Schedule with space:")
        days[inp_day] = days[inp_day]+" "+inp_activities
        write_schedule_to_file(days)

    def print_days_schedule(days):
        inp_day =(input("Enter Day Number to See Schedule:"))
        print(days[inp_day])
        # print_schedule()

    def reset_day(days):
        print("Days:\nMonday:0\nTuesday:1\nWednesday:2\nThursday:3\nFriday:4\nSaturday:5\nSunday:6\n")
        inp_day =(input("Enter Day Number to Reset:"))
        days[inp_day] = ""
        write_schedule_to_file(days)

    def write_schedule_to_file(days):
        f= open('schedule.txt','w')
        string = json.dumps(days)
        f.write(string)
        f.close()
        
    def print_schedule():
        json_file =  open('schedule.txt','r')
        days = json.load(json_file)
        print(days)
        json_file.close()
        

    while(True):
        inp = int(input("Enter choice:\n1->Scheduling \n2->Printing Schedule\n3->Reset Days Schedule\n4->Exit\n"))
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

json_file.close()
