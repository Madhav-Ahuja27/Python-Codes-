def my_generator():
    for i in range(50000000):
      # Complex computations
      yield i

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in  gen:
  print(j)
# def square(n):
#   yield n*n
#   yield n+n

# def multiply(a,b):
#   yield 25
#   yield 10
# # print(square(5))
# # print(multiply(5,5))
# _iterable=multiply(5,5)
# # for tup in _iterable:
# #   print(tup)
# print(next(_iterable))
# print(next(_iterable))
# y_itr=square(5)
# # for y in y_itr:
# #   print(y)
# print(next(y_itr))
# print(next(y_itr))

# def fib(n):
#   a=0
#   b=1
#   yield a
#   yield b
#   for i in range(n):
#     c=a+b
#     yield c
#     a,b=b,c
  



# x=fib(int(input()))
# for i in x:
#   print(i)


# a=0
# b=1
# def fib(a,b,n,i):
#   yield a
#   yield b
#   while i<n:
#     c=a+b
#     yield(c)
#     a,b=b,c
#     i+=1
#     fib(a,b,n,i)
  

# n=int(input())
# i=0
# x=fib(a,b,n,i)
# for j in x:
#   print(j)

# def addmul(a,b):
#   yield a+b
#   yield a*b

# x=addmul(5,4)
# for i in x:
#   print(i)
# lst=[1,2,43,4,34,34,34,5]
# for i in range(len(lst)-1):
#   for j in range(i+1,len(lst)):
#     if lst[i]>lst[j]:
#       lst[i],lst[j]=lst[j],lst[i]
# print(lst)
