task = input("Enter task description: ")
priority = input("What is the task's priority (high, medium, low): ")
time = input("is this task time bound? (yes or no): ")
match priority:
    case "high":
        if priority > time:
            print(f"finish {task} because it's a high priority task that requires immediate attention today!")
        else:
            print("Just do it")
    case "medium":
        if time > priority:
            print(f"finish {task} because it's time bound and that requires immediate attention today!")
        else:
            print("ok its can be deligated.")
    case "low":
        if priority < time:
            print(f"it is a {priority} priority task so you cando that late.")
        else:
            print("Do it when its necessary.")
