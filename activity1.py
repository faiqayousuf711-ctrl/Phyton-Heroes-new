#Start here
temprature = (input("Enter today's temprature in celcius: "))
new_Temprature = int(temprature)

if new_Temprature < 20:
 outfit = "Jacket"
 print("Get a jacket!")
else: 
 print("Then get a T-Shirt")

Raining = (input("To proceed, Tell me: Is it raining?(yes/no)"))
if Raining == "yes":
 is_raining = "yes" 
 print("Bring an umbrella!")
else: 
 print("Then you are fine!")

wind = (input("To continue our conversation, Tell me your wind speed in km/h: "))
new_Wind = int(wind)
if new_Wind > 30:
 needs_windbreaker = "Yes"
 print("Wear a windbreaker over your outfit in the last message(T-shirt/jacket)")
else:
 print("You are fine then!")

puddles = (input("To finally complete our weather check, tell me: Is there puddles on the ground?(yes/no)"))

if puddles == "yes":
 shoes = "boots"
 print("Wear boots")
else:
 shoes = "sneakers"
 print("Just wear some sneakers")

print ("")
print ("Weather check complete!")
print ("")

print("=========WEATHER OUTFIT PICKER==========")
print("Temprature:", new_Temprature)
print("Raining?:", Raining)
print ("Windbreaker needed?:", wind)
print ("Shoes:", shoes)
print("========================================")