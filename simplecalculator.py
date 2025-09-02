while True:
 variable1=int(input("enter the first number:"))
 variable2=int(input("enter the second number:"))
 operator=input("enter the operator(+,-,/,*):")
 if operator=="+":
    print("the sum is:",variable1+variable2)
 elif operator=="-":
    print("the difference is:",variable1-variable2)
 elif operator=="/":
    print("the division is:",round(variable1/variable2,2))
 elif operator=="*":
    print("the product is:",variable1*variable2)
 else:
    print("invalid operator")
    break
 next_calculation=input("do you want to do another calculation? (yes/no):")
 if next_calculation=="no":
    break
 elif next_calculation=="yes":
    continue
 else:
     print("invalid input") 
     break