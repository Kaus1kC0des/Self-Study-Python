"""
Exercise: a CSV to JSON converter
In the previous lectures, we learned about dealing with different formats, such as CSV and JSON. Although CSV is a very popular format of storing data, we find it so much easier to process JSON data in Python, since it's very similar to the dictionary data structure in Python.

In this exercise, we ask you to create a CSV to JSON converter that can be handy for others. You converter should achieve the following tasks:

Given a CSV file csv_file.txt with following format:

Manchester United,Manchester,UK
Real Madrid,Madrid,Spain
Juventus,Turin,Italy
Read and process the file and store its content in JSON format into json_file.txt. The according keys to each field in the CSV file are club, city and country. Thus the output should be, according to the given sample CSV file, like this:

[{"club": "Manchester United", "country": "UK", "city": "Manchester"}, {"club": "Real Madrid", "country": "Spain", "city": "Madrid"}, {"club": "Juventus", "country": "Italy", "city": "Turin"}]
PS: you may assume that the csv_file.txt file exists, and its data is always in proper format.

Happy coding!

— Jose and the Teclado team

"""
# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import json
import csv
csv_file = open('csv_file.txt', 'r')
csv_data = csv_file.readlines()
fclub = [club.strip().split(',') for club in csv_data]
input_data = []
for clubs in fclub:
    #fc = {f"{"club"}:{club[0]}, {"country"}:{club[1]}, {"city"}:{club[2]}"}
    club = clubs[0]
    country = clubs[2]
    city = clubs[1]
    fc = {"club":club,"country":country,"city":city}
    input_data.append(fc)
    #print(input_data)

json_file = open('json_file.txt', 'w')
json.dump(input_data,json_file)
json_file.close()