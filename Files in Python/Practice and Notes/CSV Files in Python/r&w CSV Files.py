import csv
movies=[
    {"name":"The Matrix","director":"Wachowski","year":1996,"success":"Hit"},
    {"name":"Green Book","director":"Farrelly","year": 1999,"success":"Floap"},
    {"name":"Amadeus","director":"Forman","year":2000,"success":"Average"}
]

"""
def write_to_file(output):
    with open("test.csv","w")as f:
        f.write("name,director,year\n")
        for line in output:
            f.write(f"{line['name']},{line['director']},{line['year']}\n")
def read_from_file():
    with open("test.csv","r")as f:
        content=f.readlines()
        for line in content[1:]:
            columns=line.strip().split(",")
            print(f"Name:{columns[0]}\tDirector:{columns[1]}\tYear:{columns[2]}")
write_to_file(movies)
read_from_file()
"""

"""
def write_to_file(output):
    with open('test.csv' ,'w') as f:
        writer = csv.writer(f)
        f.write("name","director\n")#First we're writing the header rows into the file.
        writer.writerows(elem.values() for elem in output)#Then we're writing the content into the respective columns

def read_from_file():
    with open('testt.csv' ,'w') as f:
        reader = csv.reader(f)
        for line in reader:
            print(f"Name {line[0]}\tDirector{line[1]}\tYear{line[2]}"
            
"""

def write_to_file(output):
    with open("test.csv","w")as f:
        writer = csv.DictWriter(f, fieldnames=["name", "director","year","success"])
        #DictWriter could help you write a dictionary inside a list into a file in Python.
        writer.writeheader()
        writer.writerows(output)

def read_from_file():
    with open("test.csv","r")as f:
        reader = csv.DictReader(f)
        return list(reader)
        #for line in reader:
            #print(f"Name: {line['name']}\tDirector: {line['director']}\tYear: {line['year']}")

write_to_file(movies)
read_from_file()

