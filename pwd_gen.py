#  Password generation script
import random

while(True):
    inp = int(input("enter password length(min. 8 chars):"))
    if inp >= 8:
        break
    else:
        continue
capAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallAlphabets = capAlphabets.lower()
capAlphabets+=smallAlphabets
pwd = ""
for _ in range(inp-1):
    random_char = random.randint(0,1)
    if random_char == 0:
        pwd+=str(random.randrange(0,9))
    elif random_char == 1:
        pwd+=capAlphabets[(random.randrange(0,51))]
start = random.randrange(1,len(pwd)-1)
pwd = pwd[0:start]+capAlphabets[(random.randrange(0,25))]+pwd[start:]
print("Generated Password:"+pwd)
