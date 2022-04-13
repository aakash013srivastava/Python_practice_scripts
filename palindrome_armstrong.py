# Script to print different special number cases

cases = int(input("Enter number of cases:"))
print("Select criteria from list:\n")
criteria = int(input("1.Palindrome Numbers 2.Armstrong numbers\n"))
# num = input("Enter the number:")



def call_func(cases,criteria):
    number = cases
    
    if criteria == "P":
        for x in range(1,cases+1):
            num2 = int((str(x))[::-1])
            if x == num2:
                print(x,end=" ")
    elif criteria == "A":
        for x in range(1,cases+1):
            total = 0
            x2 = x
            while x2>=1:
                total+=(x2%10)**3
                x2=x2//10
            # print(total)
            if total == x:
                print(x)





while(True):
    if criteria == 1:
        call_func(cases,"P")
        break
    elif criteria == 2:
        call_func(cases,"A")
        break
    else:
        print("Wrong choice")
        continue



