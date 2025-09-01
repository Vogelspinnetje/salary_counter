'''
Author: Yesse Monkou
Date: 01/09/2025

This script counts all hours worked per month (through an .ics file), and calculates the salary.
'''

from ics import Calendar

agenda_path = "agenda.ics"
hourly_salary = float(input("Fill in your hourly salary:"))
content = "Month\tHours\tSalary\n"
totals = {
    "January": [0, 0],
    "February": [0, 0],
    "March": [0, 0],
    "April": [0, 0],
    "May": [0, 0],
    "June": [0, 0],
    "July": [0, 0],
    "August": [0, 0],
    "September": [0, 0],
    "October": [0, 0],
    "November": [0, 0],
    "December": [0, 0]
}

with open(agenda_path, "r") as fh:
        c = Calendar(fh.read())

for event in c.events:
    duration = event.duration
    hours = duration.total_seconds() / 3600  
    month = event.begin.format("MMMM")
    if event.description:
        break_length = int(event.description) / 60
        hours -= break_length
    
    totals[month][0] += hours

for months in totals:
    totals[months][1] = totals[months][0] * hourly_salary
    content = content + f"{months}\t{totals[months][0]}\t{totals[months][1]:.2f}\n"
    
with open("overview.tsv", "w") as fh:
    fh.write(content)
