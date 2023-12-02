# st="banana"
# # for i in range(len(st)):
# #   for j in range(i+1,len(st)+1):
# #     print(st[i:j])
# lst=[st[i:j] for i in range(len(st)) for j in range(i+1,len(st)+1)]
# for i in lst:
#   print(i)

# def hello():
#   return "Hello"
# lst1=[1,2,4]
# lst=list(map(hello(),lst1))

str="Madhab"
from itertools import permutations

all_perms=["".join(p) for p in permutations(str)]
print(len(all_perms))
print(type(all_perms))

# all_combinations=[[i,j,k] for i in range(x+1) for j in range(j+1) for k in range(z+1)]
possible_combinations=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
print(possible_combinations)

from itertools import permutations
# str=f"0{str(x)}{str(y)}{str(z)}"
str="000111"
# all_perms=["".join(p) for p in permutations(str)]
for p in permutations(str):
    print(p)
