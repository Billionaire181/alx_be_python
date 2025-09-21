task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"finish {task} because it's a high priority task, Reminder: that requires immediate attention today!")
        else:
            print("Just do it")
    case "medium":
        if time_bound == "yes":
            print(f"finish {task} because it's time bound and, Reminder: that requires immediate attention today!")
        else:
            print("ok its can be deligated.")
    case "low":
        if time_bound == "yes":
            print(f"finish {task} because it's time bound and, Reminder: that requires immediate attention today!")
        else:
            print("Do it when its necessary.")
