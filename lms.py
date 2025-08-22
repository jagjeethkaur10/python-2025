#lms use case
#student information
student_id= 13
student_name= "jagjeeth kaur"
student_age= 21
quiz_score= 90
assignment_score= 95
exam_score= 80
student_attendance= 90
#arithmetic operators
#total score
total_score= quiz_score+assignment_score+exam_score
#average score
average_score= total_score/3
#relational operators
is_passed= average_score>=75
#incremental operators for attendance
student_attendance+=1
#logical operators
award_eligibility= student_attendance>=90 & is_passed

print("======STUDENT INFORMATION==========")
print(f"STUDENT ID ={student_id}")
print(f"STUDENT NAME ={student_name}")
print(f"STUDENT AGE ={student_age}")

print("======SCORE DETAILS==========")
print(f"QUIZ SCORE={quiz_score}")
print(f"ASSIGNMENT SCORE={assignment_score}")
print(f"EXAM SCORE={exam_score}")
print(f"TOTAL SCORE={total_score}")
print(f"AVERAGE SCORE={average_score}")

print("======PASSING STATUS==========")
print(f"STUDENT RESULT={is_passed}")
print(f"AWARD ELIGIBILITY={award_eligibility}")

print("======STUDENT ATTENDANCE==========")
print(f"STUDENT ATTENDENCE={student_attendance}")

