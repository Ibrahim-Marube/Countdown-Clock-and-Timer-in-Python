# Import the time module
import time

# Define a function to display the current time
def show_time():
    # Get the current time as a string
    time_now = time.strftime("%H:%M:%S", time.localtime())
    # Print the time with a message
    print(f"The current time is {time_now}")

# Define a function to create a countdown
def countdown(seconds):
    # Loop from the given seconds to zero
    for i in range(seconds, 0, -1):
        # Print the remaining seconds
        print(f"{i} seconds left")
        # Wait for one second
        time.sleep(1)
    # Print a message when the countdown is over
    print("Time's up!")

# Call the show_time function
show_time()

# Ask the user how many seconds they want to count down
seconds = int(input("How many seconds do you want to count down? "))

# Call the countdown function with the user input
countdown(seconds)

# Call the show_time function again
show_time()
