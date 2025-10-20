
classes_and_assignments = {}

class_name = ""

while class_name.upper() != "QUIT":

    class_name = input("Enter a class name or quit to stop")

    if class_name.upper() != "QUIT":

        if class_name in classes_and_assignments:
            print(f'Assignments for {class_name}: {classes_and_assignments[class_name]}')
        else:
            classes_and_assignments[class_name] = []

        assignment_name = input(f"Enter an assignment for {class_name}")
        classes_and_assignments[class_name].append(assignment_name)

for class_name in classes_and_assignments:
    print(f'Assignments for {class_name}: {classes_and_assignments[class_name]}')


def steps_to_negative(value):
    steps = 1
    while value >= 0:
        value -= steps
        print(f"It took {steps} to get to {value}")
        steps += 1
    print(f"It took {steps-1} to get to {value}")



steps_to_negative(1)


odds = 0
for numbers in range(10):
    number = int(input("enter a number 11-72"))
    while not (11 <= number <= 72):
        print('invalid')
        number = int(input("enter a number 11-72"))
    if number % 2:
        odds += 1
print(f"You entered {odds} odd numbers")
