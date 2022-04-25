# Script to implement DeQueue

from collections import deque

class Queue():
    
    
    
    def __init__(self,dq):
        self.dq = dq

    def insert_start(self,item):
        self.dq.appendleft(item)
        print(self.dq)

    def delete_start(self):
        if len(self.dq) > 0:
            popped = self.dq.popleft()
            print(popped)
        else:
            print("Queue is empty")

    def insert_end(self,item):
        self.dq.append(item)
        print(self.dq)

    def delete_end(self,item):
        if len(self.dq) > 0 :
            popped = self.dq.pop()
            print(popped)
        else:
            print("Deque is empty")

    def insert_between(self,item,loc):
        self.dq.insert(loc-1,item)
        print(self.dq)
        
    def delete_between(self,item,loc):
        if len(self.dq) > 0  and self.dq[loc-1] == item:
            self.dq.remove(loc-1)
            print(self.dq)
        else:
            print("item not present at the location")

obj = Queue(deque())


while(True):
    inp = input("Enter 1:InsertStart 2:DeleteStart 3:InsertEnd 4:DeleteEnd 5:InsertBetween 6:DeleteBetween 7:Exit\n")

    if inp == "1":
        value = int(input("Enter value to append start:"))
        obj.insert_start(value)

    elif inp == "2":
        obj.delete_start()

    elif inp == "3":
        value = int(input("Enter value to append end:"))
        obj.insert_end(value)

    elif inp == "4":
        obj.delete_end()

    elif inp == "5":
        value = int(input("Enter value to insert between:"))
        loc = int(input("Enter location:"))
        obj.insert_between(value,loc)

    elif inp == "6":
        value = int(input("Enter value to delete between:"))
        loc = int(input("Enter location:"))
        obj.delete_between(value,loc)

    elif inp == "7":
        print("Goodbye")
        break
    
    else:
        print("Wrong choice,re-enter")
        continue
