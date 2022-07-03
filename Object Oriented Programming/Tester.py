my_student = {
    'name' : 'Rolf Smith',
    'grades' : [90,87,89,98,89]
}

def average(student):
    return (f"{my_student['name']} has scored {sum(my_student['grades']) / len(my_student['grades'])}")
print(average(my_student))
