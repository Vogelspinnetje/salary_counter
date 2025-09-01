#Salary Counter
With my new job, I ran into the problem that I can't see anywhere how many hours I worked. I work irregular days and hours. I can count the hours myself, but I'm far too lazy for that. So I wrote this program.

The usage is simple:
- You export your agenda in an .ics format (with iCalendar possible via Archive -> Export, be sure to select the right agenda).
- You run the program. The program asks your hourly salary; fill it in.
- You will get a .tsv file with every month and its hours and salaries.


**ONE VERY IMPORTANT NOTE:**
I really hope for you that your employer gives you breaks. This program is also designed to subtract your break time. It’s important to do the following in case you want to apply break time:

Put your break time in the description of each single event (workday). Fill in your break time in minutes. So half an hour break time means: `30`. If you put more than only numbers, the program will bathe in its own tears.
