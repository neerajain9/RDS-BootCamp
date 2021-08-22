# Create a Python list to store your grocery list
Grocery_List = ["Milk", "Bread", "Eggs", "Peanut Butter", "Jelly"]

# Print the grocery list
print(Grocery_List)

# Change "Peanut Butter" to "Almond Butter" and print out the updated list
Grocery_List[3] = "Almond Butter"

# Remove "Jelly" from grocery list and print out the updated list
Grocery_List.remove("Jelly")

# Add "Coffee" to grocery list and print the updated list
Grocery_List.append("Coffee")
print(Grocery_List)

del[Grocery_List[2]]
print(Grocery_List)

Grocery_List.pop(2)
print(Grocery_List)

Grocery_List.pop(-1)
print(Grocery_List)

Grocery_List.append("Coffee")
Grocery_List.append("Jam")
print(Grocery_List)

Grocery_List.pop(-2)
print(Grocery_List)

Grocery_List.insert(1, "Cookie")
print(Grocery_List)