#step 1: take first number
#step 2: take second number
#step 3: ask operation
#step 4: calculate
#step 5: print result

while True:

    try:
        number1=float(input("enter first number:"))  #step 1: take first number
        number2=float(input("enter second number:")) #step 2: take second number
    except:
        print("invalid input! please enter number only")
        continue
    operation=input("enter operation(+,-,*,/):")  #step 3: ask operation

        
    if operation=="+":
        result= number1 + number2
    elif operation=="-":
        result= number1 - number2
    elif operation=="*":
        result= number1 * number2
    elif operation=="/":
        if number2 == 0:
            print("cannot divide by zero!")
            continue
        result= number1 / number2
    else: 
        print("invalid operation")
        continue
    
    #clean output(remove .0 if integer)
    if result.is_integer():
        result=int(result)
        
        print("Result:",result)
    choice=input("Do you want to continue?(yes/no):")
    if choice=="no":
        break
    
    


