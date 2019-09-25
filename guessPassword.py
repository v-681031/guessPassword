password = 'a123456'
i = 3
print('you have ', i, 'times to guess passwrod')
while i != 0:
	guess_passwrod = input('guess password: ')
	if password == guess_passwrod:
		print('you are right! Passwrod is ', password)
		break
	else:
		i = i - 1
		if i == 0:
			print('Wrong! game over!')
		else:
			print('Wrong! You have ', i, 'times to guess')
		
		