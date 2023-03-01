print("\t\t\tMonday: ")
print("Transport: ", end = "")
t1 = int(input())
print("Lunch: " , end="")
l1 = int(input())
Monday = t1 + l1

print("\t\t\tTuesday: ")
print("Transport: ", end = "")
t2 = int(input())
print("Lunch: " , end="")
l2 = int(input())
Tuesday = t2 + l2

print("\t\t\tWednesday: ")
print("Transport: ", end = "")
t3 = int(input())
print("Lunch: " , end="")
l3 = int(input())
Wednesday = t3 + l3

print("\t\t\tThursday: ")
print("Transport: ", end = "")
t4 = int(input())
print("Lunch: " , end="")
l4 = int(input())
Thursday = t4 + l4

print("\t\t\tFriday: ")
print("Transport: ", end = "")
t5 = int(input())
print("Lunch: " , end="")
l5 = int(input())
Friday = t5 + l5

print("\t\t\tSaturday: ")
print("Transport: ", end = "")
t6 = int(input())
print("Lunch: " , end="")
l6 = int(input())
Saturday = t6 + l6

print("\t\t\tSunday: ")
print("Transport: ", end = "")
t7 = int(input())
print("Lunch: " , end="")
l7 = int(input())
Sunday = t7 + l7

Weeks = []

Weeks.append(Monday)
Weeks.append(Tuesday)
Weeks.append(Wednesday)
Weeks.append(Thursday)
Weeks.append(Friday)
Weeks.append(Saturday)
Weeks.append(Sunday)

sumofelements = 0
for i in Weeks:
    sumofelements += i
print("")
print("Sum for Week: " , sumofelements)    

