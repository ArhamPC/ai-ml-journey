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

for name , score in student.items():
    Grades = Give_grade (score)
    print(name ,"-->" , score ,"-->" ,Grades )

print("Student Average " , sum(student.values()) / len(student))
print("Top Student  :" , max(student.values()))
print("Low Student  :" , min(student.values()))
