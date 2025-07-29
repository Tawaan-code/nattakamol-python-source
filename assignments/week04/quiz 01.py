def personal_info_manager():
    # Create initial person tuple
    person = ("tawan", 19, "new york", "usa")  # name, age, city, country
    hobbies = []

    while True:
        choice = input("Please select (1 display info, 2 add hobby, 3 remove, 4 update age, 5 exit): ")

        if choice == "1":
            # Display info
            print("NAME:", person[0])
            print("Age:", person[1])
            print("City:", person[2])
            print("Country:", person[3])
            print("Hobbies:", hobbies)

        elif choice == "2":
            # Add hobby
            hobby = input("What is your hobby? : ")
            hobbies.append(hobby)

        elif choice == "3":
            # Remove first hobby
            del hobbies[0]

        elif choice == "4":
            # Update age
            person_list = list(person)
            age = int(input("How old are you? : "))
            person_list[1] = age
            person = tuple(person_list)

        elif choice == "5":
            # Exit loop
            break

        else:
            print("Invalid choice. Please try again.")

# Run the function
if __name__ == "__main__":
    personal_info_manager()
