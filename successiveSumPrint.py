#3.	Write a recursive program to calculate sum of its digits. The program must display the remaining digits successively while calculating the sum. 

def calcsum(x,n):
  sum=0
  j=len(x)
  while j>=0:
    print(n[:int(j)])
    j-=1
  for number in x:
    sum+=int(number)
  return sum
  
