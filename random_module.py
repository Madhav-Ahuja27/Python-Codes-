# import random
# # random_no=random.randint(1,10)
# # print(random_no)

# list1=[]
# for i in range(10):
#     dice1=random.randint(1,6)
#     dice2=random.randint(1,6)
#     sum=dice1+dice2
#     list1.append(sum)
# print(list1)


# # print(random.random())
# # # prints value from 0 to 1
# # # 0 is included and 1 is excluded

# # range1=random.randrange(0,1)
# # print(range1)
# # difference between randint and randrange is that randint includes last value and randrange excludes last value

# # choice = random.choice(list1)
# # print(choice)
# # choices = random.choices(list1,k=5)
# # print(choices)
# # samples=random.sample(list1,k=5)
# # print(samples)

# random.shuffle(list1)
# print(list1)

# floatno=random.uniform(10,20)
# print("%.2f" %floatno)


#write a python program that illustrates the use of all functions of random module
#write a python program using a dice roll simulator (welcome message, press enter to roll a dice, You have rolled this number:, do you stil want to continue)

def dice():
    print(random.randint(1,6))
    inp2=input("Do you wish to continue?(y/n)")
    if inp2=="y":
        dice()


import random
print("Welcome!")
inp=input("Press enter to roll a dice   ")
if inp=="enter":
    dice()


import keyboard
keyboard.add_hotkey('enter',dice())
