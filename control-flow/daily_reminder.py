task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes or no): ")
priority = input("Priority (high, medium, low): ")
match priority:
    case "high":
        if priority > time_bound:
            print(f"finish {task} because it's a high priority task that requires immediate attention today!")
        else:
            print("Just do it")
    case "medium":
        if time_bound > priority:
            print(f"finish {task} because it's time bound and that requires immediate attention today!")
        else:
            print("ok its can be deligated.")
    case "low":
        if priority < time_bound:
            print(f"it is a {priority} priority task so you cando that late.")
        else:
            print("Do it when its necessary.")
