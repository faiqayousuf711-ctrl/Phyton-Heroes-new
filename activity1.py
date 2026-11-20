print ("========SMART SCHOOL DAY PLANNER========")

Day = (input("Hi! You are using SSDP, to start, what is the day today?(Monday to sunday)"))
Weather = (input("Okay, to continue, What is the weather?(Cloudy, Rainy, or sunny)"))
Homework = (input("Now finally, tell me if your homework is done(Note: Processing time will take a bit of a while(Yes/No))"))
print("")
print(f"====Your plan for {Day}====")
print("-" * 35)
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

if Weather == "sunny" and Homework == "Yes":
 print("After school: Ask Your parents if you can play games - great weather and homework is done!")

if Weather == "rainy" or Weather == "cloudy":
 print("Before going to school pack your umbrella - it might get wet outside")

if not Homework == "Yes": 
 print("Homework isn't done yet - Finish it before going outside!")

if Weather == "cloudy" and not Homework == "yes": 
 print("Best plan - Stay in, finish your homework, then ask your parents if you want to play games or watch your show")

elif Weather == "sunny" and Homework == "yes" and not (Day in ("Saturday", "Sunday")):
 print("All set for school - you are prepared!")

elif Weather == ("Saturday", "Sunday") and Homework == "yes":
 print("Great weather and day - head outside or play in and have fun!")
else:
 print("Take it one step at a time - you got this!")

print("")
print("Plan complete - Have a great day!")