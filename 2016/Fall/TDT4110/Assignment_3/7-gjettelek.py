
import random
limit=int(input('What should be the upper limit?:'))
tilfeldig_tall = random.randint(1,limit)
while True:
    guess=int(input('{} {} = '.format('Guess a number from 1 to', limit)))
    if guess<tilfeldig_tall:
        print('Guess higher!')
    else:
        print('Guess lower!')
    if guess==tilfeldig_tall:
        print('You guessed correct! The number was',tilfeldig_tall)
        break
