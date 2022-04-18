# Script to implement Stacks/Queues in python 

class Stack():
    
    def __init__(self,ls):
        self.ls = ls
    
    def push(self,*item):
        for n in range(len(item)):
            self.ls.append(item[n])
        print(self.ls)

        
    def pop_items(self,num):
        
        length = len(self.ls)
        self.ls = self.ls[:(length-num)]
        print(self.ls)



class Queue():

    def __init__(self,ls):
        self.ls = ls
    
    def enqueue(self,*item):
        for n in range(len(item)):
            self.ls.append(item[n])
        print(self.ls)
        
    def dequeue(self,num):
        if len(self.ls ) > 0:
            self.ls = self.ls[num:]
        else:
            print("Queue Already empty!!!")
        print(self.ls)
        


obj = Stack([])
ob = Queue([])

while(True):
    inp = input("Enter 1:Stack 2:Queue 3:Exit\n")
    if inp == "1":
        
        inp_stack = input("Enter 1:Push 2:Pop\n")

        if inp_stack == "1":
            stack_push_item = input("Enter item to push onto stack:")
            obj.push(int(stack_push_item))
            
        elif inp_stack == "2":
            stack_pop_item = input("Enter number of items to pop:")
            obj.pop_items(int(stack_pop_item))

        else:
            print("Wrong choice !!!")
            continue

    elif inp == "2":
        inp_queue = input("Enter 1:Enqueue 2:Dequeue\n")

        if inp_queue == "1":
            enqueue_item = input("Enter item to add to queue:")
            ob.enqueue(int(enqueue_item))
            
        elif inp_queue == "2":
            deque_item = input("Enter number of items to dequeue:")
            ob.dequeue(int(deque_item))

        else:
            print("Wrong choice !!!")
            continue

    elif inp == "3":
        break
    else:
        print("Wrong choice !!!")
        continue
