import random

game_options = ['rock', 'paper', 'scissors']
print('Hello, want to play a game of rock, paper, scissors? ')
print("""Winning Rules of the Rock paper scissor game as follows :
Rock vs paper->paper wins 
Rock vs scissor->Rock wins
paper vs scissor->scissor wins \n""")

while True:
	print('Enter an option to continue')
	print('"R" for Rock \n"P" for Paper \n"S" for Scissors \n"quit" to exit')
	user_choice = input('Your turn : ').lower()
	cpu_choice = random.choice(game_options).lower()

	if user_choice == 'r' and cpu_choice == game_options[0]:
		print(f'CPu turn : CPU is thinking.....')
		print(f'Player({game_options[0]}) : CPU({cpu_choice})')
		print('it`s a tie. play again')
	elif user_choice == 'r' and cpu_choice == game_options[1]:
		print(f'CPu turn : CPU is thinking.....')
		print(f'Player({game_options[0]}) : CPU({cpu_choice})')
		print('CPU won')
		break
	elif user_choice == 'r' and cpu_choice == game_options[2]:
		print(f'CPu turn : CPU is thinking.....')
		print(f'Player({game_options[0]}) : CPU({cpu_choice})')
		print('You won!')
		break

	elif user_choice == 'p' and cpu_choice == game_options[0]:
		print(f'CPu turn : CPU is thinking.....')
		print(f'Player({game_options[1]}) : CPU({cpu_choice})')
		print('you won!')
		break
	elif user_choice == 'p' and cpu_choice == game_options[1]:
		print(f'CPu turn : CPU is thinking.....')
		print(f'Player({game_options[1]}) : CPU({cpu_choice})')
		print('it`s a tie. play again')
	elif user_choice == 'p' and cpu_choice == game_options[2]:
		print(f'CPu turn : CPU is thinking.....')
		print(f'Player({game_options[1]}) : CPU({cpu_choice})')
		print('CPU won')
		break

	elif user_choice == 's' and cpu_choice == game_options[0]:
		print(f'CPu turn : CPU is thinking.....')
		print(f'Player({game_options[2]}) : CPU({cpu_choice})')
		print('CPU won')
		break
	elif user_choice == 's' and cpu_choice == game_options[1]:
		print(f'CPu turn : CPU is thinking.....')
		print(f'Player({game_options[2]}) : CPU({cpu_choice})')
		print('you won!')
		break
	elif user_choice == 's' and cpu_choice == game_options[2]:
		print(f'CPu turn : CPU is thinking.....')
		print(f'Player({game_options[2]}) : CPU({cpu_choice})')
		print('it`s a tie. play again')

	elif user_choice == 'quit':
		print('thanks for playing. ')
		break
	else:
		print('invalid selection')
