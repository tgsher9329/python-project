import json
from checks import *
with open('habitData.json', 'r') as habitData:
    habits = json.load(habitData)

#?  changes the color of the text and background depending on the answer, does not save it to the file only changes the color when it is going to show the table
def colorize(table):
    blackOnGreen = "\x1b[1;30;42m"
    blackOnRed = "\x1b[1;30;41m"
    reset = "\x1b[0m"
    
    #?  for each day in the month
    for day in table.keys():
        x = 0

        #?  for the length of each list of the day do this, then go to the next day
        while x <  len(table[day]):
            if table[day][x] == "YES":
                table[day][x] = (blackOnGreen + "YES" + reset)
            elif table[day][x] == "NO":
                table[day][x] = (blackOnRed + "NO" + reset)
            x += 1



#?  tells how many times that habit was completed throughout the month
def habitsCounter(table):
    x = 0
    monthlyCounts = {}

    #?  for each day in the month
    for x in table.keys():
        
        if len(table[x]) > 0:
            for habit in habits["habits"]:
                if habit not in monthlyCounts:
                    monthlyCounts[habit] = 0

                habitindex = habits["habits"].index(habit)

                if table[x][habitindex] == "YES":
                    monthlyCounts[habit] += 1

    for count in monthlyCounts.keys():
        print(f"{count}: {monthlyCounts[count]}")