# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
## File to get data from
file_to_load = os.path.join("..", "Resources", "netflix_ratings.csv")

## File to write the results into
file_to_save = os.path.join("..", "Analysis", "netflix_analysis.txt")
                            
# Open the CSV
with open(file_to_load) as netflix_data:

    # Read the file with reader function
    file_reader = csv.reader(netflix_data)
    
    header = next(file_reader)
    #header = next(file_reader)
    #header = ["Title", "Rating", "User Rating Score"]
    #print(header)
    
    # Loop through looking for the video
    #found_it =False
    for row in file_reader:
        #i +=1
        if row[0] == video:
            #found_it =True
            #print(f'{row[0], row[1], row[6]}')
            print([row[0], row[1], row[6]])
            break
    #print(f'{i}')
#    if not found_it:
    else:
        print(f'Your video "{video}" could not be found!')        