amount=0
flag=True
print("Each correct answer is awarded 100 points.")
q1=["Who is Kira?","a)Light","b)L","c)Near","d)Mello"]
q2=["What is the name of the Shinigami bound to Light?","a)Ryuk","b)Near","c)Mello","d)None of the mentioned"]
q3=["Which type of God is Ryuk?","a)Blessing","b)Love","c)Death","d)Fertility"]

for i in q1:
  print(i)
ans=input("Enter your answer: ")
if ans=="a":
  amount=amount+100
  print("Correct answer")
  print(f"Your current amount is {amount}")
else:
  print(f"Wrong answer, the amount you have won is {amount}")
  flag=False
  
if flag==True:
  for j in q2:
    print(j)
  ans=input("Enter your answer: ")
  if ans=="a":
    amount=amount+100
    print("Correct answer")
    print(f"Your current amount is {amount}")
  else:
    print(f"Wrong answer, the amount you have won is {amount}")
    flag=False

if flag==True:
  for k in q3:
    print(k)
  ans=input("Enter your answer: ")
  if ans=="c":
    amount=amount+100
    print("Correct answer")
    print(f"Congratulations! You have won {amount} points.")
  else:
    print(f"Wrong answer, the amount you have won is {amount}")
    
