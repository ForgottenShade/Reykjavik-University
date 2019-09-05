#Recieves input numbers until a negative is entered, then reports the largest number

numbers = []
access = 1
while access == 1:
    num_int = int(input("Input a number: "))
    numbers.append(num_int)
    if num_int < 0:
        print("The maximum is", max(numbers))
        access = 0



