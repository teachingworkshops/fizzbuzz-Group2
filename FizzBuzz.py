while True:
    userInput = input('What is the max number? ')
    try:
        max_number = int(userInput)  # Convert userInput to an integer and store it in max_number.
        break
    except ValueError:  # It's good practice to specify the exception type.
        print('Enter a number')

for i in range(1, max_number):
    if i %15 == 0:
        print('FizzBuzz', end=' ')
    elif i%3 == 0:
        print('fizz', end=' ')
    elif i % 5 ==0:
        print('buzz', end=' ')
    else:
        print(i, end = ' ')
