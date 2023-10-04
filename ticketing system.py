print("Welcome to Roller-coaster")
height = int(input("What is your height? "))
age = int(input("What is your age? "))
photo_option = input("Do you want to take a photo during the ride? (yes/no): ").strip().lower()
bill = 0

if height >= 120:
    print("You can Ride")

    if age < 12:
        bill = 5
    elif 12 <= age <= 18:
        bill = 7
    elif 45 <= age <= 55:
        # Free ride for ages 45 to 55
        pass
    else:
        bill = 12

    if photo_option == "yes":
        bill += 3  # Add 3 dollars for the photo

    print(f"Your ticket price is {bill} Dollars")
else:
    print("You cannot ride")
