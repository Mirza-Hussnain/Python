import datetime

def get_greeting():
    current_hour = datetime.datetime.now().hour

    if 0 <= current_hour < 6:
        return "Good night"
    elif 6 <= current_hour < 12:
        return "Have a good day"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good night"

user_name = input("Enter your name: ")
greeting = get_greeting()

current_time = datetime.datetime.now().strftime("%H:%M:%S")

print(f"{greeting}, {user_name}! The current time is {current_time}.")
