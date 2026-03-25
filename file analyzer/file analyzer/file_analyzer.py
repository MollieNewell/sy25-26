import glob

files = glob.glob("server_dump/*.txt") 

warn = 0
ok = 0
error = 0 
sat_1 ="WARN"
sat_2 = "OK"
sat_3 = "ERROR" 
warn_name = []
ok_name = []
error_name = []

for i in files:
    file = open(i, "r")
    content = file.read()
    if sat_1 in content:
        warn += 1
        warn_name.append(i)
    elif sat_2 in content:
        ok += 1
        ok_name.append(i)
    elif sat_3 in content:
        error += 1  
        error_name.append(i)
    else:
        print("UNKNOWN STATUS FOR FILE: " + file)

print("WARN: " + str(warn))
print("OK: " + str(ok))
print("ERROR: " + str(error))   

choice = input("Would you like to see your files for a status?: ")
if choice == "yes":
    type = input("Which status would you like to see? (WARN, OK, ERROR): ")
else:
    print("Goodbye!")   
    
if type == "WARN":
    print("WARN FILES: " + str(warn_name))
elif type == "OK":
    print("OK FILES: " + str(ok_name))
elif type == "ERROR":
    print("ERROR FILES: " + str(error_name))
else:
    print("UNKNOWN STATUS")

file.close