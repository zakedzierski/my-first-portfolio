import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)


# Start your search algorithm here.
inputcon = input("Type a country")
lowerBound = 0
upperBound = 31
midpoint = 16
while lowerBound != upperBound:
    if inputcon == countries[midpoint]:
        print("Yes!")
        break
    elif inputcon < countries[midpoint]:
        upperBound = (midpoint - 1)
    elif inputcon > countries[midpoint]:
        lowerBound = (midpoint + 1)
