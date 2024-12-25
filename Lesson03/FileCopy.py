# Define a function named file_copy that takes two arguments: src (source file) and dest (destination file).
scr = "FileCopy.py"
dest = "z.py"
def file_copy(src, dest):
    # Use the 'with' statement to open the source file for reading ('r') and the destination file for writing ('w').
    with open(src) as f, open(dest, 'w') as d:
        # Read the content of the source file and write it to the destination file.
        d.write(f.read())

# Call the file_copy function with the source file "untitled0.py" and the destination file "z.py".
file_copy("FileCopy.py", "z.py")

# Use the 'with' statement to open the 'z.py' file for reading ('r').
with open('z.py', 'r') as filehandle:
    # Iterate through the lines in the 'z.py' file.
    for line in filehandle:
        # Print each line, and specify 'end' as an empty string to avoid extra line breaks.
        print(line, end = '')