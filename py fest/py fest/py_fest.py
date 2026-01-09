
# The initial lineup
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]

# 1. Add the headliner
headliner = ("The Byte Beats", "Synthwave", 90)
lineup.append(headliner)

# Continue the logic below...
rb = lineup.pop(0)
lineup.append(rb)
lineup.remove(("The Pythonistas", "Rock", 45))

total_time = 0
for band in lineup:
    total_time += band[2]  # Add the duration of each band's performance

print(lineup)
print(f"Total time for Py-Fest: {total_time} minutes")
