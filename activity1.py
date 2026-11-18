print ("========SMART SCHOOL DAY PLANNER========")

Day = (input("Hi! You are using SSDP, to start, what is the day today?(Monday to sunday)"))
Weather = (input("Okay, to continue, What is the weather?(Cloudy, Rainy, or sunny)"))
Homework = (input("Now finally, tell me if your homework is done(Note: Processing time will take a bit of a while(Yes/No))"))

if Day in ("Saturday", "Sunday"):
 print ("Its the weekand! Enjoy your free time!")
elif Day == ("Monday"):
 print("First day of the week! Stay sharp")
elif Day == ("Friday"):
 print("Last day, flip canteen chairs on the tables and pray Jumma prayer")
elif Day == ("Tuesday", "Wednesday", "Thursday"):
 print("Okay, seems like its a regular day, Focus!")
else:
 print("Day not recognized, please check your spelling or do upper case")