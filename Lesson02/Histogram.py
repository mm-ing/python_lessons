import random

class clsHistogram: # Define a class called Histogram.
    def __init__(self, character='*'):
        self.character = character
        self.items = []
        self.items.append(character)
    # Define a function called histogram that takes a list of items as a parameter.
    def draw(self):
        # Iterate through the items in the list.
        for n in self.items:
            output = ''  # Initialize an empty string called output.
            times = n     # Set the times variable to the value of n.
            
            # Use a while loop to append '*' to the output string 'times' number of times.
            while times > 0:
                output += self.character
                times -= 1  # Decrement the times variable.
            
            # Print the resulting output string.
            print(output)
        print('---------------------------------') # Print a separator line at the end of the histogram.
        return

# Call the histogram function with a list of numbers and print the histogram.
histogram = clsHistogram() # create an instance of the Histogram class with default character '*'
histogram.items = [random.randint(1, 50) for x in range(10)] # create 10 random nos between 1 and 50 into the items list
histogram.draw() # draw the histogram 

histogram.character = 'X' # change the histogram character to 'X'
histogram.draw()

histogram.character = 'O' # change the histogram character to 'O'
histogram.draw()


