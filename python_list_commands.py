'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the
types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''

list_of_elements = []
command_count = int(input("Enter the number of commands:"))
counter = 0
for _ in range(command_count):
    
        cur_command_input = str(input("Enter operation on list:"))
        cur_command_input_split = cur_command_input.split(' ')
        command = cur_command_input_split[0]
        if(len(cur_command_input_split)==3):
            list_of_elements.__getattribute__(command)(int(cur_command_input_split[1]),int(cur_command_input_split[2]))
        if(len(cur_command_input_split)==2):
            list_of_elements.__getattribute__(command)(int(cur_command_input_split[1]))
        if(len(cur_command_input_split)==1 and cur_command_input_split[0] != "print"):
            list_of_elements.__getattribute__(command)()
        if "print" in command:
            print(list_of_elements)
