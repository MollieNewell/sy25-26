all_potatoes = [0,2,5,1,0,8,3,0]
perfect_potatoes = []
for p in all_potatoes:
    if p ==0:
        perfect_potatoes.append(p)
total = len(all_potatoes)
perfect = len(perfect_potatoes)
percent = (perfect/total) * 100
print(f"Percentage of perfect potatoes: {percent}%")