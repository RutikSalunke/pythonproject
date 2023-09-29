print("+,-,*,/")
num1=int(input("Enter the Number:-----"))
num2=int(input("Enter the Number:-----"))
operator=input("Enter the Operator:----")
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("Invalid Operator.........")   