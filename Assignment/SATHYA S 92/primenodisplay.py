l = int(input("Limit: "))

print("The Prime Numbers in the given limit: ")
for number in range(1, l + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)