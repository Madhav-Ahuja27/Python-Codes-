#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

import random
user=int(input("Enter 0 for snake, 1 for water, 2 for gun"))
computer=random.randint(0,2)
if computer==0:
  computer1="Snake"
elif computer==1:
  computer1="Water"
else:
  computer1="Gun"

if user==0:
  print("You chose Snake")
  print(f"Computer chose {computer1}")
elif user==1:
  print("You chose Water")
  print(f"Computer chose {computer1}")
elif user==2:
  print("You chose Gun")
  print(f"Computer chose {computer1}")
else:
  print("Wrong input detected")

if (user==0 and computer==0) or (user==1 and computer==1) or (user==2 and computer==2):
  print("Its a draw")
elif (user==0 and computer==2) or (user==1 and computer==0) or (user==2 and computer==1):
  print("You win")
elif (user==0 and computer==1) or (user==1 and computer==2) or (user==2 and computer==0):
  print("You lose")
else:
  print("Something went wrong")
