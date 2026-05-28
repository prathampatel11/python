subject_1 =float(input("enter subject_1 mark ="))
subject_2 =float(input("enter subject_2 mark ="))
subject_3 =float(input("enter subject_3 mark ="))
subject_4 =float(input("enter subject_4 mark ="))
subject_5 =float(input("enter subject_5 mark ="))

total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
print(total)

percentage = (total / 500) * 100
print(percentage)

if percentage>=90:
    print("your grade is A+")

elif percentage>=80 and percentage<=89:
    print("your grade is A")

elif percentage>=70 and percentage<=79:
    print("your grade is B")

elif percentage>=60 and percentage<=69:
    print("your grade is C")

elif percentage>=50 and percentage<=59:
    print("your grade is D")

else:
    print("you are need to improve")