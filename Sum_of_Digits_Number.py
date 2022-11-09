#this program is about printing the sum of all digits in a user-given number

try:
    num = input("Enter a number: ")
    sum = 0
    for digit in num:
        sum += int(digit)
    print(f"The sum of all digits in {num} is {sum}")
except Exception as e:
    print("Enter a number not character.")
