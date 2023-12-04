# i is for rows and j is for columns
# Universal count:
n = 5

# Basic Square

for i in range(n):
  for j in range(n):
    print("*",end=" ")
  print()

#Increasing Triangle  (MOST IMPORTANT #1)

for i in range(n):
  for j in range(i+1):
    print("*",end=" ")
  print()

# Decreasing Triangle  (MOST IMPORTANT #2)

for i in range(n):
  for j in range(i,n):
    print("*",end=" ")
  print()

# ALL PATTERNS ARE A COMBINATION OF THESE 2

# Increasing Right Sided Triangle

for i in range(n):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  print()

# Decreasing Right Sided Triangle

for i in range(n):
  for j in range(i+1):
    print(" ",end=" ")
  for j in range(i,n):
    print("*",end=" ")
  print()

# Hill Pattern (MOST IMPORTANT #3)

for i in range(n):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i):
    print("*",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  print()

# Reverse Hill Pattern

for i in range(n):
  for j in range(i+1):
    print(" ",end=" ")
  for j in range(i,n):
    print("*",end=" ")
  for j in range(i,n-1):
    print("*",end=" ")
  print()

# Diamond

for i in range(n-1):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i):
    print("*",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  print()

for i in range(n):
  for j in range(i+1):
    print(" ",end=" ")
  for j in range(i,n):
    print("*",end=" ")
  for j in range(i,n-1):
    print("*",end=" ")
  print()

# Double Hill

for i in range(n):
  for j in range(i,n):
    print(" ",end="")
  for j in range(i):
    print("*",end="")
  for j in range(i+1):
    print("*",end="")

  for j in range(i,n-1):
    print(" ",end="")

  for j in range(i,n):
    print(" ",end="")
  for j in range(i):
    print("*",end="")
  for j in range(i+1):
    print("*",end="")
  print()

# Basic Pyramid

for i in range(n):
  for j in range(i,n):
    print(" ",end="")
  for j in range(i+1):
    print("*",end=" ")
  print()

# Double Pyramid

for i in range(n):
  for j in range(i,n):
    print(" ",end="")
  for j in range(i+1):
    print("*",end=" ")

  for j in range(i,n-1):
    print(" ",end="")

  for j in range(i,n-1):
    print(" ",end="")
  for j in range(i+1):
    print("*",end=" ")
  print()

# Reverse Pyramid

for i in range(n):
  for j in range(i+1):
    print(" ",end="")
  for j in range(i,n):
    print("*",end=" ")
  print()

# Butterfly (INCOMPLETE)

for i in range(n-1):

  for j in range(i+1):
      print("*",end=" ")
  for j in range(i,n-2):
    print(" ",end=" ")
  for j in range(i,n-2):
    print(" ",end=" ")
  for j in range(i+1):
      print("*",end=" ")
  print()

for i in range(n):
  if i!=0:
    for j in range(i,n):
      print("*",end=" ")
  else:
    for j in range(i,n):
      print("*",end=" ")
    print("",end="")

  if i!=0:
    for j in range(i):
      print(" ",end=" ")
    for j in range(i):
      print(" ",end=" ")

  else:
    for j in range(i):
      print(" ",end=" ")
    for j in range(i):
      print(" ",end=" ")

  if i!=0:
    for j in range(i,n):
      print("*",end=" ")
  else:
    # print(" ",end=" ")
    for j in range(i,n):
      print("*",end=" ")

  print()

# Sandglass

for i in range(n):
  for j in range(i + 1):
    print(" ", end="")
  for j in range(i, n):
    print("*", end=" ")
  print()

for i in range(n):
  for j in range(i, n):
    print(" ", end="")
  for j in range(i + 1):
    print("*", end=" ")
  print()

## HOLLOW PATTERNS

# Hollow square side bars

for i in range(n):
  for j in range(n):
    if j==0 or j==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()


# Hollow square center plus

for i in range(n):
  for j in range(n):
    if j==n//2 or i==n//2:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()


# Hollow square center cross

for i in range(n):
  for j in range(n):
    if j==i or i+j==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()


# Hollow square 

for i in range(n):
  for j in range(n):
    if j==0 or i==0 or i==n-1 or j==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()


# Hollow Increasing Triangle

for i in range(n):
  for j in range(i+1):
    if j==0 or i==j or i==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()


# Hollow Decreasing Triangle

for i in range(n):
  for j in range(i,n):
    if i==0 or j==0 or j==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()


# Hollow Hill Pattern

for i in range(n):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i+1):
    if j==0 or i==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  for j in range(i):
    if j==i-1 or i==n-1:
      print("*",end=" ")
    else:
     print(" ",end=" ")
  print()


## Final Boss - Hollow Diamond 

for i in range(n-1):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i):
    
    if j==0:
      print("*",end=" ")
    else:
      print(" ",end=' ')
  
  for j in range(i+1):
    if i==j:
      print("*",end=" ")
    else:
      print(" ",end=' ')
  print()

for i in range(n):
  for j in range(i+1):
    print(" ",end=" ")
  for j in range(i,n-1):
    if j==i:
      print("*",end=" ")
    else:
      print(" ",end=' ')
  for j in range(i,n):
    if j==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()


## NUMBER PATTERNS


# Basic same number increasing triangle

for i in range(n):
  for j in range(i+1):
    print(1,end=" ")
  print()


# Increasing number increasing triangle

p=1
for i in range(n):
  for j in range(i+1):
    print(p,end=" ")
  p+=1
  print()


# Increasing number increasing triangle

p=5
for i in range(n):
  for j in range(i+1):
    print(p,end=" ")
  p-=1
  print()


#Increasing number increasing triangle

p=0
for i in range(n):
  for j in range(i+1):
    print(p,end=" ")
  p+=2
  print()


# Alternating number increasing triangle

for i in range(n):
  for j in range(i+1):
    if i%2==0:  
      print(1,end=" ")
    else:
      print(2,end=" ")
  print()


# Increasing columns increasing triangle

for i in range(n):
  p=1
  for j in range(i+1):
    print(p,end=" ")
    p+=1
  print()


# Floyd Triangle (Very Important)

p=1
for i in range(n):
  for j in range(i+1):
    print(p,end=" ")
    p+=1
  print()
