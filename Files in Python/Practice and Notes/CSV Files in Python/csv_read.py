file = open('csv_data.txt', 'r')
lines = file.readlines()
lines = [line.strip() for line in lines[1:]]
"""
Here we are stripping the whitespaces from the lines file, and we are reading only from the 2nd line 
which ignores the first line which contains name,age,school,degree
"""
for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    school = person_data[2].upper ()
    degree = person_data[3].title()
    #print(f"Hello this is {name}")
    print(f"This is {name} is {age}, studying {degree} at {school}.")

sample_csv_data = ','.join(['kausik', '18','Harvard','MBA'])
#The .join here will join the elements of the string with the character you had provided inside the ''
#So if you replace the "," with ":", your data will look something like this
#kausik:18:Harvard:MBA
print(sample_csv_data)