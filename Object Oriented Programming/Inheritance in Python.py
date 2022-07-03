class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


anna = Student("Anna", "Oxford")

"""
Imagine you’ve got a class like the above, and you want to create a similar class with some extra functionality. For example, a student that not only has marks but also a salary—a `WorkingStudent`:
"""

"""
class WorkingStudent:
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary

    def average(self):
        return sum(self.marks) / len(self.marks)

    def weeklysalary(self):
        #Here we are going to calculate the weekly salary of a student.
        #In India the weekly working hours is 40
        return self.salary * 40


rolf = WorkingStudent("Rolf", "MIT", 15.50)
"""


"""
However you can see there’s a lot of duplication between our `Student` and `WorkingStudent` classes. Instead, we may choose to make our 
 `WorkingStudent` extend the `Student`. It keeps all the same functionality, but we can add more.
"""

"""The Student class attributes are inherited into the WorkingStudent Class by putting it as WorkingStudent(Student). 
This WorkingStudent is  a child of the Student Class.
"""

"""class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


rolf = WorkingStudent("Rolf", "MIT", 15.50)
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average())
"""

"""
Use of Decorators in Python. 
"""

class WorkingStudent:
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary

    def average(self):
        return sum(self.marks) / len(self.marks)
    @property
    def weeklysalary(self):
        #Here we are going to calculate the weekly salary of a student.
        #In India the weekly working hours is 40
        return self.salary * 40

"""
Here if we want to call the weekly salary we can do print(kausik.weeklysalary())
But the curly braces here bring in a lot of ambiguity. So we might prefer print(kausik.weeklysalary)
This is possible when we use decorators. Here we have used the @property  decorator.
"""
kausik = WorkingStudent("Kausik","STJEC",25)
#print(kausik.weeklysalary()) is replaced by the below code.
print(kausik.weeklysalary)
