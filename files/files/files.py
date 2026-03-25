file_name = "output.txt"
file = open(file_name, "a")
for i in range(10):
    file.write(f"{i+1} Hello, World!\n")
file.close()