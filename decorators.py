
def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)

def greet(fx):
  def mfx(*args,**kwargs):
    print("hello")
    fx(*args,**kwargs)
    print("The above statement contains the sum")
  return mfx
@greet
def sum(a,b):
  print(a+b)

sum(1,2)
