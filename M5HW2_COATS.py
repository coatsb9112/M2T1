# Brandon Coats
# CTI 110
# 10/22/17
# M5HW2

total=0
for i in range(5):
    newNumber = int (input("Enter a number: " ))
    if newNumber < 0:
        break
    total += newNumber
print("The total is: ",total)
