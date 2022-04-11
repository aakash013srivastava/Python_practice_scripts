import random

def number_guess():
    rewards = [("Cake","IceCream","Chocolate"),("Macbook","XPS","DSLR"),("Iphone","Galaxy","One+")]
    inp = int(input("Enter a number,if correct you get a reward and goto next level:"))
    generated_num = random.randrange(1,4)
    level_num = 1
    if(inp == generated_num):
        print("You get a: {}".format(rewards[level_num-1][random.randrange(1,4)]))
        level_num =2
        inp2 = int(input("Enter a number,if correct you get a reward and goto level 3:"))
        generated_num2 = random.randrange(1,4)
        if(inp2 == generated_num2):
            print("You get a: {}".format(rewards[level_num-1][random.randrange(1,4)]))
            level_num =3
            inp3 = int(input("Enter a number,if correct you get a reward and goto level 3:"))
            generated_num3 = random.randrange(1,4)
            if(inp3 == generated_num3):
                print("You get a: {}".format(rewards[level_num-1][random.randrange(1,4)]))
            else:
                print("Your Guess was incorrect")
        else:
            print("Your Guess was incorrect")
    else:
        print("Your Guess was incorrect")


number_guess()