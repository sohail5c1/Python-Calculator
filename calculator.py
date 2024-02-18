
#.......CALCULATOR........

#creating func for operations...
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

while True:
    #choice to choose a num
    print("1.add,2.sub,3.mul,4.div")
    choice = int(input("choose any of in 1/2/3/4 " ))
    
    if choice in (1,2,3,4):
        try:
            num1 = int(input("enter the first number:"))
            num2 = int(input("enter the second number:"))

        except ValueError:
            print("invalid input,please enter the correct number")
            continue
        if choice == 1:
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == 2:
            print(num1,"-",num2,"=",sub(num1,num2))
        elif choice == 3:
            print(num1,"*",num2,"=",mul(num1,num2))
        elif choice == 4:
            print(num1,"/",num2,"=",div(num1,num2))
        
        next_cal = int(input("enter 0 to exit and 1 to continue " ))
        if next_cal == 0:
            break

    else:
        print("Invalid input")

