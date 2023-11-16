# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


word=input("Enter your word")
newword=""
cod=input("Do you want to code or decode? c/d")
if cod=="c":
  if len(word)>3:
    newword=word[1:]
    newword+=word[0]
    newword="fst"+newword+"lst"
    newword=newword[::-1]
    print(newword)
  else:
    newword=word[::-1]
    print(newword)
else:
  if len(word)<3:
    newword=word[::-1]
  else:
    newword=word[3:]
    newword3=newword[:-3]
    newword2=newword3[:len(newword)-1]
    newword2=newword3[-1]+newword2
    print(newword2)
