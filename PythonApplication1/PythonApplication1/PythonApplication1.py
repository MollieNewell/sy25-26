import datetime

# Define your morning routine tasks with estimated durations in minutes
routine = [
    {"task": "Wake up", "duration": 7},
    {"task": "Use reastroom", "duration": 2},
    {"task": "Brush teeth", "duration": 2},
    {"task": "Wash face",  "duration": 7},
    {"task": "Do makeup", "duration": 15},
    {"task": "Get dressed", "duration": 13},
    {"task": "Pack lunch", "duration": 12},
    {"task": "Eat breakfast", "duration": 12},
    {"task": "Pack bag", "duration": 3},
]

# Set your desired wake-up time
wake_up_time_str = input("Enter your wake-up time (HH:MM, 24-hour format): ")
wake_up_time = datetime.datetime.strptime(wake_up_time_str, "%H:%M")

# Calculate schedule
current_time = wake_up_time
schedule = []

for item in routine:
    start_time_str = current_time.strftime("%H:%M")
    end_time = current_time + datetime.timedelta(minutes=item["duration"])
    end_time_str = end_time.strftime("%H:%M")
    schedule.append({"task": item["task"], "start": start_time_str, "end": end_time_str})
    current_time = end_time

# Display the schedule
print("\nYour morning routine schedule:")
for entry in schedule:
    print(f"{entry['task']}: {entry['start']} - {entry['end']}")

# Finished
print("TIME TO GET GOING!")