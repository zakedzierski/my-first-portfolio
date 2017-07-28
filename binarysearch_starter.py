import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)


# Start your search algorithm here.

inputcon = input("Type a country:")
lowerBound = 0
upperBound = (length - 1)
midpoint = 16


while lowerBound != upperBound:
    if (inputcon < countries[midpoint]) and (inputcon != countries[lowerBound]):
        upperBound = (midpoint - 1)
        midpoint = ((lowerBound + upperBound) // 2)
    elif (inputcon > countries[midpoint]) and (inputcon != countries[upperBound]):
        lowerBound = (midpoint + 1)
        midpoint = ((lowerBound + upperBound) // 2)
    else:
        print("Yes!")
        break

if lowerBound == upperBound:
    print("No!")import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)


# Start your search algorithm here.

inputcon = input("Type a country:")
lowerBound = 0
upperBound = (length - 1)
midpoint = 16


while lowerBound != upperBound:
    if (inputcon < countries[midpoint]) and (inputcon != countries[lowerBound]):
        upperBound = (midpoint - 1)
        midpoint = ((lowerBound + upperBound) // 2)
    elif (inputcon > countries[midpoint]) and (inputcon != countries[upperBound]):
        lowerBound = (midpoint + 1)
        midpoint = ((lowerBound + upperBound) // 2)
    else:
        print("Yes!")
        break

if lowerBound == upperBound:
    print("No!")
