from random import randint
random_integer = randint(1,101)
print('----------- About the Game -----------')
print('1. Make a guess b/w 1 and 100')
print('2. If your guess within 10, we tell you that your guess WARM; else if further than 10, then COLD')
print('3. Closer to the previous guess WARMER')
print('4. Farther from the previous guess COLDER')
print('5. If matched, I will tell you the number of guesses it took you')
guesses = [0]
print(random_integer)
while True:
    guess = int(input('Make a valid guess b/w 1 and 100: '))
    if(guess >=1 and guess<= 100):
        guesses.append(guess)
        if(guesses[-1] == random_integer):
            print(f'CONGRATS!! you got the correct guess in {len(guesses) - 1}')
            break
        if(guesses[-2] == 0):
            if(abs(guess - random_integer) <= 10):
                print('Warm')
            else:
                print('Cold')
        else:
            if(abs(guess - random_integer) <= abs(guesses[-2] - random_integer)):
                print('Warmer')
            else:
                print('Colder')
    else:
        print('Not a valid guess')