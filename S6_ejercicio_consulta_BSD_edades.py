
# Define a list of client ages
clients = [19, 22, 42, 28, 69, 51, 18, 70]

# Initialize a variable to store the count of clients found
clients_found = 0

# Iterate through each client age in the list
for age in clients:
    # Check if the client age is greater than 21 and less than 60
    if age > 21 and age < 60:
        # If the condition is met, increment the clients_found counter
        clients_found += 1

# Print the count of clients found
print(clients_found)
#
#In this code, we define a list of client ages and initialize a variable to store the count of clients found. We then iterate through each client age in the list and check if the client age is greater than 21 and less than 60. If the condition is met, we increment