# @TODO: Your code here

# Create a dictorany Called Pets

pet = dict()
pet ={"name": "Ugly", 
       "age": 9, 
       "Hobbies": ["biting","sleeping", "eating", "tricks"], 
       "Wakeup": {"Mon": "3 am", "Tue": "4 am", "Wed": "2 am"}
       }
print(f"My dog's name is {pet['name']} and he is {pet['age']} years old.")
print(f"My dog has {len(pet['Hobbies'])} hobbies.")
print(f"My dog's favorite hobby is {pet['Hobbies'][0]}.")
print(f"My dog wakes up at {pet['Wakeup']['Mon']} on Mondays.")

print(f"My Dog's name is {pet['name']} and he is {pet['age']} years old. His hobbies are {pet['Hobbies'][0]} and {pet['Hobbies'][1]} and on Mondays he wakes up at {pet['Wakeup']['Mon']}.")     