task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that needs to be completed today.")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that should be done today.")
    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")