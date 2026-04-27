
name = input("Enter Your Name ")
weight = float(input("Enter Your Weight "))
height = float(input("Enter Your Height"))


def calculate_BMI (weight , height):
    bmi = weight / (height** 2)
    return bmi

def dec_BMI (bmi):
    if bmi < 18.5:
        return "Under Weight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Over Weight"
    else:
        return "Obese"

print("Hi! ", name)
bmi = calculate_BMI (weight , height)
print("Your BMI is " , round(bmi))
desc = dec_BMI (bmi)
print("You are ", desc )


