"""
Objects are things of a special type that have data and functions inside them.
Object are preceded by something called CLASS.
Class defines the functions and parameters for an object, once done we can operate on Object using these Classes.
"""

#Lets look at a class and an object here.

class Student:
    def __init__(self,new_name,new_grades):
        self.name=new_name
        self.grades=new_grades
    """Here '__init__' denotes that its a dunder function. Self is a blank object which was created before we called the dunder function
    ,new_name and new_grades are parameters upon which the object is operated"""
    """The .name an .grade are used to assign a variable called name and grade to the blank object called self. self.name will provide
    a variable called name to the data, and self.grade will assign a variable called grade for the data of that particular parameter"""

    #The variable inside an object is no longer a varianle, its called a property of an object.

    def average(self):
        return sum(self.grades)/len(self.grades)
    """The average function is not a function. It is to be called as a method.
    A method is a function that “belongs to” an object. And here 'self' can be named as anything you want. It could be anything 
    like 'student', 'person', etc. But generally the word self is a convention.
    """

student_one= Student('Kausik D', [83,61,81,81,83])
student_two= Student('Nandhini S', [100,100,100,100,100])
print(student_two.average())
print(student_one.average())
"""print(student_one.name)
print(student_one.grades)
print(student_one.__class__)"""

def average(student):
    return sum(student.grades)/len(student.grades)

print(average(student_one))

"""
so the average function outside the class also could be called upon the object we use.
That is we are accessing the property(variable of an object) to operate upon it.
"""


