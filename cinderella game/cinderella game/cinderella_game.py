seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
winners = ['Purdue', 'FDU', 'FAU', 'Memphis', 'Duke', 'Oral Roberts', 'UVA', 'Furman', 'Kentucky', 'Pitt', 'Kansas', 'Howard', 'Texas', 'Penn St', 'UCLA', 'UNC Asheville']

cinderellas = 0

for i,s in enumerate(seeds):
    if s >= 10:
        print(f"Cinderalla Alert! {winners[i]} pulls the upset!")
        cinderellas += 1
print(f"Total Cinderalla teams: {cinderellas}")
