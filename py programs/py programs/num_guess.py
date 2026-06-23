import random as r
print('🎉Welcome to the lucky number game!🎉')
print("I'm thinking of a number between 1 and 20...\nCan you guess it?" )
tryy=0
play='yes'
best_score=1000
while play=='yes':
	num=r.randint(1,20)
	tryy=0
	s=0
	while s==0:
		guess=int(input('\nEnter you guess:'))
		tryy=tryy+1
		if guess>num:
			print('Too high! Try again.')
		elif guess<num:
			print('Too low! Try again.')
		else:
			print(f'🎯Correct! You guessed it in {tryy} tries.')
			if tryy<best_score:
				best_score=tryy
			play=input('Do you want to play again? (yes/no):')
			play=play.lower()
			s=s+1			
print(f'Thanks for playing, Your best score was {best_score} tries.🏆')				
