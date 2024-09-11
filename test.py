#code for printing fizz when the number is divisible by 3 
n = int(input("Enter the length: "))
for i in range(1,n):
    if (i%3==0):
        print("fizz")
    else:
        print(i)