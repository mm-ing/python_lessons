import sys

isSimpleExtendedIP = False

folderName = "c:/Git/PythonLessons/Lessons/Lesson04/"
fileRawExtension = "Raw"
fileSolvedExtension = "Cleaned"
fileExtension = "txt"

ipsRussianFederation = "IP_RussianFederation"
ipsMissellaneous = "IP_Miscellaneous"

if isSimpleExtendedIP:
    fileName = ipsRussianFederation
else:
    fileName = ipsMissellaneous

fileNameFrom = f"{folderName}{fileName}-{fileRawExtension}.{fileExtension}"
fileNameTo = f"{folderName}{fileName}-{fileSolvedExtension}.{fileExtension}"

print(fileNameFrom)

# to check file name
#pause = input("Press Enter to continue...")

# Open a file in read-write mode ('r' mode)
with open(fileNameFrom, 'r') as file:
    
    file.seek(0) # Move the cursor back to the beginning of the file    

    # Step 3: Read the data from the file

    #read first line
    content = file.readlines()

    #create a list to store the ip addresses
    ipSet = set()
    startIp = 0
    endIp = 255

    #loop through the content
    for line in content:     
        if isSimpleExtendedIP:
            #split the line into single words with space as delimiter
            words = line.split()
            wordLine = f"{words[0]}-{words[1]}"
        else:
            #split the line into single words with = as delimiter
            wordsRaw = line.split('=')
            if len(wordsRaw) < 2: continue
            words = wordsRaw[1].split('&')
            if len(wordsRaw) < 2: continue
            ipSplit = words[0].split('.')    
            if len(ipSplit) < 4: continue        
            wordLine = f"{ipSplit[0]}.{ipSplit[1]}.{ipSplit[2]}.{startIp}-{ipSplit[0]}.{ipSplit[1]}.{ipSplit[2]}.{endIp}"           

        print(wordLine)
        #pause = input("Press Enter to continue...")

        # Add the IP address to the set (duplicates will be ignored)
        ipSet.add(wordLine)

    # Convert the set back to a list if needed
    ipList = list(ipSet)

    # Print the count of unique IP addresses
    print(f"Total unique IP addresses: {len(ipList)}")

    #open the file in write mode    
    file = open(fileNameTo, 'w')

    file.seek(0) # Move the cursor back to the beginning of the file

    #loop through the ipList
    for ip in ipList:
        #write the ip to the file
        file.write(ip + "\n")

    file.close()
    print(f"File {fileNameTo} has been created.")

# Exit the program with a status code
sys.exit(0)  # Successful termination


