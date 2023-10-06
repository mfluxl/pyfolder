
letter = "F"
grade = " "

gradepercentage = float(input("What is your grade? "))

if gradepercentage >= 90:
    letter = "A"
elif gradepercentage >= 80:
    letter = "B"
elif gradepercentage >= 70:
    letter = "C"
elif gradepercentage >= 60:
    letter = "D"
elif gradepercentage < 60:
    letter = "F"
print(letter)

###
last_digit = gradepercentage % 10

sign = " "

if gradepercentage >= 97 or gradepercentage < 60:
    sign = ""
elif last_digit >= 7:
    sign = "+"
elif last_digit > 3:
    sign = "-"
else:
    pass

print(sign)
###

if gradepercentage >= 70:
    print("Congratulations! You pass the class!")
else:
    print("You did not pass. Better luck next time!")

### sign:



