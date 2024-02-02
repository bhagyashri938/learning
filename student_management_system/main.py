#student information system/main.py
from student import Student
from course import Course
from grade_calculator import calculate_gpa
#create students
student1=Student("001","Piyush")
student2=Student("002","Trijal")
#create courses
ds_couses=Course("DS01","Data Science 101")
da_couses=Course("DS01","Data Analytics 102")
#Entroll student in couses
student1.add_course(ds_couses,90)
student1.add_course(da_couses,85)
student2.add_course(ds_couses,78)
student2.add_course(da_couses,92)
#Display student information
print(f"{student1.name}'s Grades:{student1.get_grades()}")
print(f"{student2.name}'s Grades:{student2.get_grades()}")
#calculate and display GPA
gpa_student1=calculate_gpa(student1.get_grades())
gpa_student2=calculate_gpa(student2.get_grades())
print(f"{student1.name}'s GPA:{gpa_student1:.2f}")
print(f"{student2.name}'s GPA:{gpa_student2:.2f}")
