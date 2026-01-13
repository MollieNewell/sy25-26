print("---Py-fest 2026 stage manager---")
print("1.View lineup and total time")
print("2. Add a new band")
print("3. Move first band to end")
print("4.Remove a band by name")
print("5. Move band to specifive position")
print("6. Exit")
choice = input("Select an option (1-6):")

if choice == "1":
    print("/n---current Lineup---")
    lineup = [
        ("Code Play", "Indie", 30)
        ("The Pythonistas", "Rock", 45)
        ("Syntax Error" , "Metal", 60)
    ]
    for i, artist in enumerate(lineup,1):
        name, genre, duration, = artist
        print(f"{i}. {name} {genre} - {duration} mins")

    total_time = 0
    total_time += duration
    print(f"Total festival duration: {total_time} minutes")

elif choice == "2":
    name = input("enter name of band: ")
    genre = input("enter genre of band:")
    duration = int(input("enter duration of band (in minutes): ")
    lineup.append((name, genre, duration))

elif choice == "3":
    late_band = lineup.pop(0)
    lineup.append(late_band)
    print(f"{late_band[0]} has been moved to the end of the lineup.")

elif choice == "4":
    name_to_remove = input("enter the name of the band to remove: ")
    for artist in lineup:
        if artist[0].lower() == name_to_remove.lower():
            lineup.remove(artist)
            print(f"{name_to_remove} has been removed from the lineup.")
            break
    else:
        print(f"{name_to_remove} not found in the lineup.")

elif choice == "5":

elif choice == "6":
    print("exiting stage manager. have a great show!")
else:
    print("Please enter a valid option (1-6)")
