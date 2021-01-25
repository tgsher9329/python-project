import json
from checks import *
with open('habitData.json', 'r') as habitData:
    habits = json.load(habitData)

def colorize(table):
    blackOnGreen = "\x1b[1;30;42m"
    blackOnRed = "\x1b[1;30;41m"
    reset = "\x1b[0m"

    # try to add a counter to see how many days there is a yes to give how many days in the month each habit was completed
    
    for day in table.keys():
        x = 0

        while x <  len(table[day]):
            if table[day][x] == "YES":
                table[day][x] = (blackOnGreen + "YES" + reset)
            elif table[day][x] == "NO":
                table[day][x] = (blackOnRed + "NO" + reset)
            x += 1



# this gives the number of completed habtis each day
def habitsCounter(table):
    x = 0
    monthlyCounts = {}

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