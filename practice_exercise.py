#Print all odd numbrs fro, 1 to 20 
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

#Print multiples of 57
i = 57
while i<=570 :
    print(i)
    i += 57

#Print all multiples of 3 from 1 to 50 but skip 15
i = 3
for i in range (1,50):
    if i % 3 == 0:
        if i == 15:
            continue
        print(i)

#Take two integer a and b as input .Find and print the first number between 1 and 1000 that is divided by both numbers 

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
        print(f"The first number between 1 and 1000 that is divisible by both {a} and {b} is: {i}")
        break