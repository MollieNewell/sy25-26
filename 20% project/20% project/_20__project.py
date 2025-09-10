from datetime import datetime, timedelta

def get_morning_routine():
    routine = []
    print("Enter your morning routine tasks. Type 'done' when finished.")
    while True:
        task = input("Task name (or 'done'): ").strip()
        if task.lower() == 'done':
            break
        try:
            duration = int(input(f"How many minutes does '{task}' take? "))
        except ValueError:
            print("Please enter a valid number for minutes.")
            continue
        routine.append({'task': task, 'duration': duration, 'completed': False})
    return routine

def get_times():
    while True:
        wake_up = input("Enter your wake-up time (HH:MM, 24-hour format): ").strip()
        leave = input("Enter your leave time (HH:MM, 24-hour format): ").strip()
        try:
            wake_up_time = datetime.strptime(wake_up, "%H:%M")
            leave_time = datetime.strptime(leave, "%H:%M")
            if leave_time <= wake_up_time:
                print("Leave time must be after wake-up time.")
                continue
            return wake_up_time, leave_time
        except ValueError:
            print("Please enter times in HH:MM format.")

def organize_routine(routine):
    # Sort tasks by duration (shortest first)
    return sorted(routine, key=lambda x: x['duration'])

def display_routine(routine, wake_up_time, leave_time):
    print(f"\nYou wake up at: {wake_up_time.strftime('%H:%M')}")
    print(f"You leave at: {leave_time.strftime('%H:%M')}")
    print("\nYour organized morning routine:")
    current_time = wake_up_time
    total_time = 0
    for idx, item in enumerate(routine, 1):
        end_time = current_time + timedelta(minutes=item['duration'])
        status = "[X]" if item['completed'] else "[ ]"
        print(f"{idx}. {status} {item['task']} - {item['duration']} minutes ({current_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')})")
        current_time = end_time
        total_time += item['duration']
    print(f"Total time needed: {total_time} minutes")
    if current_time > leave_time:
        print("Warning: Your routine exceeds your available time before leaving!")

def check_off_tasks(routine, wake_up_time, leave_time):
    while True:
        display_routine(routine, wake_up_time, leave_time)
        incomplete = [i for i, item in enumerate(routine) if not item['completed']]
        if not incomplete:
            print("All tasks completed!")
            break
        try:
            choice = input("Enter the number of the task you finished (or 'done' to exit): ").strip()
            if choice.lower() == 'done':
                break
            idx = int(choice) - 1
            if idx in incomplete:
                routine[idx]['completed'] = True
            else:
                print("Task already completed or invalid number.")
        except ValueError:
            print("Please enter a valid task number or 'done'.")

if __name__ == "__main__":
    routine = get_morning_routine()
    wake_up_time, leave_time = get_times()
    organized = organize_routine(routine)
    check_off_tasks(organized, wake_up_time, leave_time)