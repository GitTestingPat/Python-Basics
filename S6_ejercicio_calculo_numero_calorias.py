
# Define a dictionary to store the calorie values of different food items
calories = {
   "Hamburguesa": 600,
   "Hamburguesa con queso": 750,
   "Hamburguesa vegetariana": 400,
   "Hamburguesa vegana": 350,
   "Batatas": 230,
   "Ensalada": 15,
   "Té helado": 70,
   "Limonada": 90,
}

# Define a function to calculate the total calories of three food items
def calories_counter(item_a, item_b, item_c):
    # Use the dictionary to look up the calorie values of the three food items
    # Add the calorie values together to get the total calories
    # Return the total calories
    return calories[item_a] + calories[item_b] + calories[item_c]

# Call the function with three food items as arguments
# The function will calculate the total calories of these food items and print the result
print(calories_counter("Ensalada", "Hamburguesa con queso", "Té helado"))
#
#This code defines a dictionary called `calories` to store the calorie values of different food items. It then defines a function called `calories_counter` that takes three food items as arguments. The function uses the dictionary to look up the calorie values of the three food items, adds these values together to get the total calories, and returns the total calories. Finally, the code calls the