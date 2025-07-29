def number_operations():
    numbers = []

    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        num = int(input("Enter number [" + str(i) + "]: "))
        numbers.append(num)  # แก้จาก numbers[i] เป็น append()

    # Display original list
    print(f"Original numbers: {numbers}")

    # Create filtered lists
    even_numbers = []
    odd_numbers = []

    # Calculate average
    average = sum(numbers) / len(numbers)

    # Numbers greater than average
    above_average = []

    # Display results
    for i in range(10):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
        else:
            odd_numbers.append(numbers[i])

        if numbers[i] > average:
            above_average.append(numbers[i])

    print("Even Numbers: ", even_numbers)
    print("Odd Numbers: ", odd_numbers)
    print("Above Average: ", above_average)
    print("Sum: ", sum(numbers))
    print("Average: ", average)
    print("Min: ", min(numbers))
    print("Max: ", max(numbers))

    print("Even number")  # อันนี้ไม่จำเป็น แต่ถ้าอยากให้แสดงก็ปล่อยไว้ได้

if __name__ == "__main__":
    number_operations()
