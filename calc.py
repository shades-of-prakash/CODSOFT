def add(a,b):
    return a+b;
def sub(a,b):
    return a-b;
def div(a,b):
    return a/b;
def mul(a,b):
    return a*b;
def display(a):
    print('Rseult:{}'.format(a))
try:
    while(True):
        a=int(input('Enter first number'))
        b=int(input('Enter second number'))
        print('Enter your Choice')
        choice=int(input('1.Addtion\n2.Subtraction\n3.Multiplication\n4.Division\n'))
        if(choice==1):
            res=add(a,b)
            display(res)
        elif(choice==2):
            res=sub(a,b)
            display(res)
        elif(choice==3):
            res=mul(a,b)
            display(res)
        else:
            res=div(a,b)
            display(res)
        userChoice=input('Do you want to continue(y/n)')
        if(userChoice.lower()=='n'):
            break
        else:
            continue
except:
    print('exception Raised')
