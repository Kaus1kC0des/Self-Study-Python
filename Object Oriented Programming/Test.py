"""class Movie:
    def __init__(self,name,year):
        self.name = name
        self.year = year

matrix = Movie("The Matrix", 1994)
print(matrix.name)
print(f"The name of the movie is '{matrix.name}' and was released on {matrix.year}")
"""

"""movie = ['Matrix', 'Finding Nemo']
print(movie.__class__)
print(len(movie))

class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

ford_garage = Garage()
ford_garage.cars.append('Fiesta')
ford_garage.cars.append('Focus')
print(ford_garage.cars)

class Mov:
    def __init__(self):
        self.name = []

movies = Mov()
movies.name.append("Vikram")
movies.name.append("The Shawshank Redemption")
movies.name.append("Master")
movies.name.append("Maanagaram")
print(movies.name)"""

class Garage:
    def __init__(self):
        self.cars = []
        self.make = []
        self.price = []

    def __len__(self):
        return len(self)

    def __getitem__(self,i):
        return self[i]

    #def __repr__(self):
        #return f"<Garage {self}"

    def __str__(self):
        return f"Garage has {self.cars} cars"

ford = Garage()
ford.cars.append("Focus")
ford.make.append("Ford")
ford.price.append("$6000")
ford.cars.append("Fiesta")
ford.make.append("Ford")
ford.price.append("$10000")
"""print(ford.price)
print(ford.cars[0])
print(ford.price[1])
print(ford)


name = "reshma"
print(f"Hello {name}")


leng = [1,2,3,4,5,6]
lengd = (lambda x: x + x)(leng)
print(lengd)"""

class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        self.salary = salary
        self.marks = []

kausik = WorkingStudent("Kausik","STJEC",10000)
print(kausik.salary)
kausik.marks.append(100)
kausik.marks.append(10)
kausik.marks.append(100)
print(kausik.average())