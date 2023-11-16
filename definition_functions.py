# used to display the output of the argument passed.(print)
#len is used to return the length of a sequence
#input is used to read the input from the user via keyboard
l1=[1,2,3,4,5,6,7,8]
# print(sum(l1))
# print(pow(l1[4],l1[1]))
# print(round(3.14874747474,2))
print(list(reversed(l1)))
x=-10
print(abs(x))
#abs(absolute) returns the positive value of any number.
#callable() displays true or false for a function or object is callable or not.
print(callable(x))
print(bin(5))
#bin is used for binary value of a number. It is always prefixed with 0b.
#hex converts decimal to hexadecimal or octastring
print(hex(15))
#any() and all() function checks if any or all elements in an iterable are true
l2=[1,2,4,5,6,7.4,4,5,4,0]
print(any(l2))
print(all(l2))
#slice function is used to get a slice object that can be used to slice sequences/iterables
string2="my name"
print(string2)
string2[2]="g"
