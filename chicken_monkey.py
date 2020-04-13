numbers = range(1, 101)
print(numbers)

for number in numbers:
    if number % 5 == 0 and number % 7 == 0:
        print("ChickenMonkey")
    elif number % 5 ==0:
        print("Chicken")
    elif number % 7 == 0:
        print("Monkey")
    else:
        print(number)