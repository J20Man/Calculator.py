import inquirer 


#Takes the users input
first_input = int(input("Enter your first number "))
second_input = int(input("What is your second number? "))

questions = [
  inquirer.List('occurance',
                message="What would you like to do to your number?",
                choices=['Add', 'Subtract', 'Multiply', 'Divide'],
            ),
]
answers = inquirer.prompt(questions)

#addition
if answers['occurance'] == 'Add':
    output = first_input + second_input
    print(output)

#subtraction
if answers['occurance'] == 'Subtract':
    output = first_input - second_input
    print(output)
    
#multiplication
if answers['occurance'] == 'Multiply':
    output = first_input * second_input
    print(output)

#division
if answers['occurance'] == 'Divide':
    output = first_input / second_input
    print(output)