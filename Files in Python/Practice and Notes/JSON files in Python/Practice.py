import json
"""
READING FROM A JSON FILE:

1) Open the file.
2) Use the json.load() to read(load) the data from the JSON file.
3) Close the file.
"""
file = open('friends_json.txt', 'r') #This is a file pointer which points to the friends_json.txt
file_contents = json.load(file)#Now we're loading contents from the file using the file pointer
#This reads the file and also converts it into a dictionary.. Now file_contents is a dictionary.
print(file_contents['friends'][0])
file.close()

#LOAD stands for READ.

"""
WRITING TO A JSON FILE:

1) Open the file.
2) Use the dump function to input the string into the JSON file.
3) Close the file.
"""
cars_json = open('cars_json.txt', 'w')
cars = [
    {"make":"Kia","model":"Carens"},
    {"make":"Maruti Suzuki","model":"Ertiga"}
]
json.dump(cars, cars_json) #DUMP stands for write.
cars_json.close()

"""
CONVERTING JSON STRING (String in JSON format) INTO A DICTIONARY:

1) Open the file.
2) Use the json.loads(). loads stands for load_string.
3) Close the file
"""
my_json_string = '[{"make":"Hyundai", "model":"Creta"}]'
#loads allows us to turn a JSON STRING into a dictionary.
car = json.loads(my_json_string)
print(car[0]['make'])

"""
CONVERTING A DICTIONARY TO A STRING:

1) Open the file.
2) Use the json.dumps() to convert a dictionary into a JSON String.
3) JSON dumps() stands for dump_string
4) Dumps will turn a dictionary into a JSON string.
"""
cars = [
    {"make":"Kia","model":"Carens"},
    {"make":"Maruti Suzuki","model":"Ertiga"}
]
my_cars = json.dumps(cars)
#print(f"This is {cars[1]['make']} {cars[1]['model']}")
print(my_cars)