from datetie import datetime

def display_current_datetime():
    NOW = datetime.datetime.now()
    current_date = NOW.strftime("%Y-%m-%D")
    print(f"current date: {current_date}")

def calculate_future_date(days):
    today_date = datetime.now()
    days = int(input("Enter the number of days to add to the current date: "))
    time_gap = timedelta(days)
    future_date = today_date + time_gap
    formatted_future_date = future-date.strftime("%Y-%m-%D")
    print(f"future date : {formatted_future_date}")

display_current_datetime()
calculate_future_date(days)
