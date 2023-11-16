def calculate_score(data):#creating a function to calculate the scores from data given by the user
    assignment_scores = data["assignment"]
    theory_test_scores = data["theory_test"]
    lab_test_scores = data["lab_test"]
    mini_project_score = data["mini_project"]
    
    total_assignment_score = sum(assignment_scores)
    total_theory_test_score = sum(theory_test_scores)
    total_lab_test_score = sum(lab_test_scores)
    
    total_score = (total_assignment_score * 0.1) + (total_theory_test_score * 0.25) + (total_lab_test_score * 0.15) + (mini_project_score * 0.1)
    
    return total_score# returing to the main function after calculating the total score

def calculate_grade(score):#creating a function to calculate the grade
    if score >= 90:
        return "S"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    elif score >= 35:
        return "E"
    else:
        return "F"

def calculate_class_average(data_list):#creating a function to calculate the class average
    total_scores = sum(data["total_score"] for data in data_list)
    class_average = total_scores / len(data_list)
    return class_average

def calculate_average_grade(grade_list):#creating a function to calculate the average grade
    total_grades = sum(grade_list)
    average_grade = total_grades / len(grade_list)
    return average_grade

# Input student data
students = []#creating  a list to store data
for i in range(5):#creating a dictionary to collect the student data
    student_data = {}
    student_data["name"] = input(f"Enter name of Student {i+1}: ")
    student_data["assignment"] = [int(x) for x in input("Enter assignment scores ( ): ").split()]
    student_data["theory_test"] = [int(x) for x in input("Enter theory test scores ( ): ").split()]
    student_data["lab_test"] = [float(x) for x in input("Enter lab test scores ( ): ").split()]
    student_data["mini_project"] = int(input("Enter mini project score: "))
    students.append(student_data)

for student in students:#to sort single student data from collected data
    total_score = calculate_score(student)
    student["total_score"] = total_score
    grade = calculate_grade(total_score)
    student["grade"] = grade

class_avg = calculate_class_average(students)
grade_list = [student["total_score"] for student in students]
avg_grade = calculate_average_grade(grade_list)

print("\nStudent Data:")
for student in students:#printing the student data using dictionary
    print(f"{student['name']}: Total Score = {student['total_score']}, Grade = {student['grade']}")

print(f"\nClass Average Score: {class_avg}")#printing class average
print(f"\nAverage Grade: {avg_grade}")#printing average grade 
