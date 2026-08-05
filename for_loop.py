#for loop : A for loop is a control flow statement that allows code to be executed repeatedly based on a given sequence. The for loop can be thought of as a repeating if statement. The code inside the loop will continue to execute for each item in the sequence.

# 0 to 4 
nums = range(5)
for i in nums:
    print(i)

#0 to 10
for num in range(11):
    print(num)

#1 to 10 even numbers
for i in range(1 ,11):
    if i % 2 == 0 :
        print(i)

for i in range (0,11,2):
    print(i)