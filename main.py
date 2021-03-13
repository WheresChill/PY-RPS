import random

print('Lets Play!')
myAnswer = input()


options = ['rock', 'paper', 'scissors']

rando = random.choice(options)
print(rando)

if rando == myAnswer:
  print('Its a tie! Lets play again...')
elif myAnswer == 'rock' and rando == 'scissors':
  print('🎉 You win!')
elif myAnswer == 'paper' and rando == 'scissors':
  print('I win!')
elif myAnswer == 'rock' and rando == 'paper':
    print('I win!')
elif myAnswer == 'scissors' and rando == 'paper':
    print('🎉 You win!')
elif myAnswer == 'paper' and rando == 'rock':
    print('🎉 You win!')
elif myAnswer == 'scissors' and rando == 'rock':
    print('I win!')
