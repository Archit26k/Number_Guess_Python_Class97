print('Number Guessing Game')
chances = 0
while chances < 5:
    guess = int(input('guess the number (1-9)'))
    number = 8
    if(guess == number):
        print('Congratulation you have won')
        break
    elif(guess < number):
        print('Your Expectation is low ')
        chances = chances+1
    else:
        print('Your expectation is little high')
        chances = chances+1
if(chances == 5):
    print('You lose, the number is ' , number)