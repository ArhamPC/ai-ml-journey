student = {
    "Aqib" : 90,
    "Pupi" : 70,
    "Moma" : 92,
    "Gidi" : 87,
    "Sany" : 55
}

def Give_grade (score):
    if score >= 90:
        return "Grade A"
    elif score >= 80:
        return "Grade B"
    elif score >= 70:
        return "Grade C"
    elif score >= 60:
        return "Grade D"
    else:
        return "Grade F"
    
with open ("result.txt" , "w") as file:
        file.write("<---Result Card--->\n")
        for name , score in student.items():
            grade = Give_grade (score)
            line = name + "-->" + str(score) + "-->" + grade + "\n"
            file.write(line)
        file.write("=== End of Report ===\n")

print( "Results Saved in Given File! ")

print("/n Reading the file! ")
with open("result.txt" , "r") as file:
    readness = file.read()
    print(readness)

