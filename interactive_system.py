if __name__=="__main__":
    name=input("What is your name?")
    import time
    hour=int(time.strftime("%H")).
    if hour>0 and hour<12:
        greet="Good Morning"
    elif hour>=12 and hour<=16:
        greet="Good Afternoon"
    elif hour>=16 and hour<20:
        greet="Good Evening"
    else:
        greet="Good Night"
    print(greet,name+"!")
    print('''What would you like to do? Type the corresoponding keyword to use the programs:''')
    run1=input('''Calculator:calc,Time:t, age:a, second converter:sc turtles:turt, pattern:p, leap year:leapyr, bmi:bm Table:tab--->''')

def calc(first,second,operator):
    first=int(first)
    second=int(second)
    if operator=="+":
            print(first + second)
    elif operator=="-":
            print(first - second)
    elif operator=="*":
            print(first * second)
    elif operator=="/":
            print(first / second)
    elif operator=="%": 
            print(first % second)
    elif operator=="**":
            print(first**second)
    elif operator=="//":
            print(first//second)
    else: print("Invalid operator")
        
    if __name__=="__main__":
        def table(n=1):
            i=1
            n=int(n)
            while i<=10:
                print(n,"X",i,"=",i*n)
                i=i+1
            
            
        if run1=="calc":
            first = input("Enter first number")
            second = input("Enter second number")
            print("Press the following keys to select the operator: + , - , * , / , % , ** , // ")
            operator=input("Enter operator:")
            calc(first,second,operator)    

        if run1=="tab":
            n=input("Enter the number to print the table")
            table(n)
            
            
        if run1=="t":  
            t = time.strftime("%H:%M:%S", time.localtime())
            print("Current Time is :", t)
            
        if run1=="a":
            age=int(input("What is your age?"))
            if age<=12:
                print("You are a kid", name)
            elif age>12 and age<18:
                print("You are a teenager", name)
            elif age>18 and age<50:
                print("you are an adult", name)
            else:
                print("You are quite aged", name)

        if run1=="turt":
            import turtle
            sc=turtle.Screen()
            bgc=input("Enter the background color for the screen    ")
            sc.bgcolor(bgc)
            t1=turtle.Turtle()
            c=input("Enter the color of the turtle     ")
            ts=input("Enter shape of the turtle        ") 
            ps=int(input("Enter the pen size for turtle    "))
            sp=int(input("Enter speed of the animation     "))
            t1.pensize(ps)
            t1.color(c)
            t1.shape(ts)
            t1.speed(sp)

            shape=input("What type of shape would you like to draw? sq,rect,tri,spiral")
            if shape=="square":
                for i in range(4):
                    t1.forward(150)
                    t1.left(90)
                # t1.forward(150)
                # t1.left(90)
                # t1.forward(150)
                # t1.left(90)
                # t1.forward(150)
                # t1.left(90)
            if shape=="rectangle":
                for i in range(4):
                    t1.forward(150)
                    t1.left(90)
                # t1.forward(75)
                # t1.left(90)
                # t1.forward(150)
                # t1.left(90)
                # t1.forward(75)
                # t1.left(90)
            if shape=="triangle":
                for i in range(3):
                    t1.forward(150)
                    t1.left(120)
                # t1.forward(150)
                # t1.left(120)
                # t1.forward(150)
                # t1.left(120)
            if shape=="spiral":
                times=int(input("Enter number of times to draw"))
                distance = 50
                for _ in range(times):
                    t1.forward(distance)
                    t1.right(90)
                    distance = distance + 10
                t1.right(180)
        if run1=="sc":
            inputsec=int(input("Enter the number of seconds to be converted:"))
            hours=inputsec // 3600
            sec_remain=inputsec % 3600
            sec_to_mins=sec_remain // 60
            sec_still_remain=sec_remain % 60
            print("hours:",hours,"minutes:",sec_to_mins,"seconds:",sec_still_remain)
        if run1=="p":
            sy=input("Enter the symbol")
            rows=int(input("Enter no of rows"))
            k=0
            for i in range(1,rows):
                for l in range(1,(rows-i)+1):
                    print(' ',end="")
            while k!=(2*i-1):
                print(sy,end="")
                k+=1
            k=0
            print()

        def bmi(h,w):
            pass
        def leapyr(yr):
            if int(yr)%4==0:
                print("The specified year is a leap year")
            else:
                print("The specified year is NOT a leap year")

        if run1=="leapyr":
            year=int(input("Enter the year"))
            leapyr(year)

        def fib(f):
            times=0
            n1=0
            n2=1
            while(times<=f):
                print(n3)
                n3=n1+n2
                n1=n2
                n2=n3
                times+=1
        if run1=="fb":
            f=int(input("Enter number of times to run"))
            fib(f)
