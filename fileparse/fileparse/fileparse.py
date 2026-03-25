file_name = input("What is the name of the file to parse?:")
file = open(file_name, 'r')
word = input("What word are you looking for?:")
count = 0



line = file.readline()

while line:
    if word.upper() in line.upper():
        count += line.upper().count(word.upper())
    line = file.readline()


print(f"Searching for {word} in {file_name}...")
print(f"{word} appears {count} times in {file_name}.")