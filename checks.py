import json

with open('yearData.json', 'r') as yearData:
    year = json.load(yearData)
with open('habitData.json', 'r') as habitData:
    habits = json.load(habitData)

#?  check to see if the month they want to see if there is anything in the days, if not tell them to enter a day, or multiple days
#? if the len of each day added together is longer than 0 then go to the table
def monthLengthCheck(month):
    length = 0
    for i in year[month]:
        if (len(year[month][i]) > 0):
            length += 1
        else:
            length = length

    return length

def errorMessage():
    print("Invalid option, check your answers.")

def habitLengthCheck(habits):
    if len(habits) > 0:
        return True
    
    else:
        return False