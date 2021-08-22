# Initial variable to track game play
user_play = "y"

start_range = 0
# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    input_numbers = int(input("How many numbers?: "))
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for i in range(start_range, start_range+input_numbers):
        
        # Print each number in the range
        print(i)
  
    start_range = start_range + input_numbers
    #start_range = i+1

    #print(start_range)    
     # Once complete...
    user_play = input("Continue: (y)es or (n)o? : ")