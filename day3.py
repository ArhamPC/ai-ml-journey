print("Welcome to Arhms Calculator")
      
num1 = (float(input("Enter Number A: ")))
operator = (input("Enter Operator to Calculate +-x :"))
num2 = (float(input("Enter Number B: ")))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "/":
    if num2 == 0:
        result = "no devisible"
    else:
        result = num1 / num2

else:
    result = "No Given Operator Selected"



print("Answer is" , result)


    
    



