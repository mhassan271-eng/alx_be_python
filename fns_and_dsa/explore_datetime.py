from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date():
    try:
        # لازم تكون الجملة دي بالضبط حرفيًا
        days_to_add = int(input("Enter the number of days to add to the 
current date: "))
    except ValueError:
        return "Invalid input. Please enter a number."

    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    return future_date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    current = display_current_datetime()
    print("Current date and time:", current)

    future = calculate_future_date()
    print("Future date:", future)

