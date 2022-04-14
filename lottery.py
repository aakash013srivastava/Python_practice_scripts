# Lottery ticketing system 

ls = []


def create_queue(ls):
    name = input("Enter name:")
    num = int(input("Enter the queue number:"))
    ls.append((num,name))


def add_to_queue(ls):
    name = input("Enter name:")
    num = ls[len(ls)-1][0]+1
    ls.append((num,name))

def delete_from_queue(ls):
    name = input("Enter name:")
    num = int(input("Enter the queue number:"))
    ls.remove((num,name))


def insert_between_queue(ls):
    empty_slots = {}
    ls2 = [x for x in range(1,ls[len(ls)-1][0])]
    # print(ls)
    ls_slots = [x for x,y in ls ]
    empty_slots = set(ls2) - set(ls_slots)
    name_inp = input("Enter name to provide ticket:")
    num = empty_slots.pop()
    # print(num)
    # print(ls)
    if num < ls[0][0]:
        start = tuple((num,name_inp))
        start = [start]
        print(start)
        print(ls)
        start.extend(ls)
        ls = start
        print(ls)
    else:
        ls.insert(num,(num,name_inp))
    # print(ls)


def print_queue(ls):
    if len(ls) > 0:
        for num,name in ls:
            print(str(num)+":"+name)
    else:
        print("Queue empty")

while(True):
    try:
        choice = int(input("Enter 1:Add 2:Delete 3:Insert Between 4:Print Queue 5:Exit\n"))
    except:
        print("Please check input format")
        continue
    else:
        if choice == 1:
            if len(ls) == 0:
                create_queue(ls)
            else:
                add_to_queue(ls)
        elif choice == 2:
            delete_from_queue(ls)
        elif choice == 3:
            insert_between_queue(ls)
        elif choice == 4:
            print_queue(ls)
        elif choice == 5:
            print("Goodbye")
            break
        else:
            print("Wrong choice")
            continue
