# Define a function called histogram that takes a list of items as a parameter.
def histogram(items):
    # Iterate through the items in the list.
    for n in items:
        output = ''  # Initialize an empty string called output.
        times = n     # Set the times variable to the value of n.
        
        # Use a while loop to append '*' to the output string 'times' number of times.
        while times > 0:
            output += '*'
            times = times - 1  # Decrement the times variable.
        
        # Print the resulting output string.
        print(output)

# Call the histogram function with a list of numbers and print the histogram.
histogram([2, 3, 6, 5])