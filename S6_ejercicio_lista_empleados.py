
# Define the QA team and the development team
qa_team = ['Jordan Lee', 'Alex Patel']
dev_team = ['Taylor Nguyen', 'Casey Johnson']

# Create a list of teams, which includes the QA team and the development team
department = [qa_team, dev_team]

# Print the title of the output
print('Empleados:')

# Iterate through each team in the department list
for team in department:
    # Iterate through each name in the current team
    for name in team:
        # Print the name of the employee
        print(name)
#
#In this code, we define two teams: the QA team and the development team. Each team is represented as a list of strings, where each string is the name of an employee.
#
#We then create a list of teams, which includes the QA team and the development team. This list is called `department`.
#
#We print the title of the output, which is "Empleados:".
#
#Next, we iterate through each team in