
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y;
if __name__ =="__main__":
    num1=float(input("ENTER NUM1: "))
    num2 = float(input("ENTER NUM2: "))
    result1= add(num1,num2)
    print(result1)
    result2= sub(num1,num2)
    print(result2)
    result3= mul(num1,num2)
    print(result3)
    result4= div(num1,num2)
    print(result4)

