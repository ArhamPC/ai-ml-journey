student = ["Aqib" , "Ahmad" , "Faiz" , "Raza" , "Peer"]
scores = [85 , 92 , 60 , 45 , 78]
print("=== Student Grade Report ===")
for i in (range(len(student))):
    child = student[i]
    numb = scores[i]

    if numb >= 90:
        grade = "A"
    elif numb >= 80:
        grade = "B"
    elif numb >= 70:
        grade = "C"
    elif numb >= 60:
        grade = "D"
    else:
        grade = "F"
    print(child , "-->" , numb , "-->" , grade)

print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))

