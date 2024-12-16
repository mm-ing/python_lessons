import sys
import ipaddress

folderName = "c:/Git/PythonLessons/Lessons/Lesson04/"
fileRawExtension = "Unsorted"
fileSolvedExtension = "Sorted"
fileExtension = "txt"

fileName = "IP_Adresses"

fileNameFrom = f"{folderName}{fileName}-{fileRawExtension}.{fileExtension}"
fileNameTo = f"{folderName}{fileName}-{fileSolvedExtension}.{fileExtension}"

print(fileNameFrom)

# to check file name
#pause = input("Press Enter to continue...")

# Open a file in read-write mode ('r' mode)
with open(fileNameFrom, 'r') as file:
    
    file.seek(0) # Move the cursor back to the beginning of the file

    #read first line
    content = file.readlines()

    #create a list to store the ip addresses
    ipSet = set()
    ipList = []

    #loop through the content
    for line in content:
        # Remove the newline character at the end of the line
        cleaned_line = line[:-2]
        #split line to list
        splittedLine = cleaned_line.split('-')
        # Add the IP address to the set (duplicates will be ignored)
        ipList.append(splittedLine) 
        # print(splittedLine)
        # pause = input("Press Enter to continue...")
            # Validate the IP address
        try:
            ipaddress.ip_address(splittedLine[0])
            ipaddress.ip_address(splittedLine[1])
            # Add the IP address to the list (duplicates will be ignored)
            ipList.append(splittedLine)
        except ValueError:
            print(f"Invalid IP address found: {splittedLine}")
        continue

    # ipAddress = ipaddress.ip_address(ipList[0][0])
    # print(f"IP Address: {ipAddress}")
    # print(f"IP Address Raw: {ipList[0]}")
    # pause = input("Press Enter to continue...")

    # Convert the IP addresses to ipaddress objects and sort them
    ipsSorted = sorted(ipList, key=lambda ip: ipaddress.ip_address(ip[0]))

    for ip in ipsSorted:
        ipString = f"{ip[0]}-{ip[1]}"
        ipSet.add(ipString) 

    #print the sorted list
    for ip in ipSet:
        print(ip)

    #open the file in write mode    
    file = open(fileNameTo, 'w')

    file.seek(0) # Move the cursor back to the beginning of the file

    #loop through the ipList
    for ip in ipSet:
        #write the ip to the file
        file.write(ip + "\n")

    file.close()
    print(f"File {fileNameTo} has been created.")
    
# Exit the program with a status code
sys.exit(0)  # Successful termination