print("Enter Marks obtained in 5 subjects")

markone = int(input())
marktwo = int(input())
markthree = int(input())
markfour = int(input())
markfive = int(input())

total = markone + marktwo + markthree + markfour + markfive
avg = total/5

print(total)
print(avg)

validrange = range(0, 101)

if avg not in validrange:
    print("Invalid output. Marks must be above 0 and below 100")


elif avg in range(91, 101):
 print("Your grade is A1")


elif avg in range(81, 91):
 print("Your grade is A2")

elif avg in range(71, 81):
 print("Your grade is B1")


elif avg in range(61, 71):
 print("Your grade is B2")

elif avg in range(51, 61):
 print("Your grade is C1")

elif avg in range(41, 51):
 print("Your grade is C2")

elif avg in range(31, 41):
 print("Your grade is D1")

elif avg in range(21, 31):
 print("Your grade is D2")

elif avg in range(11, 21):
 print("Your grade is F1")

elif avg in range(1, 11):
 print("Your grade is F2")
