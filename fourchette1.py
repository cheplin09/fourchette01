import time
import random

print('\nJeu de la fourchette !\nVous devez deviner un nombre entre 1 et 100')

y = random.randint(1, 100)
#print(str(y))

time.sleep(3)
print('\nEntrer un nombre:')
x = int(input())

while (x != y):

	if x < y :
		print('trop petit') 
	if x > y :
		print('trop grand') 
	time.sleep(3)
	print('\nEntrer un nombre:')
	x = int(input())

print('\n *************** Bravo ! **************\n') 

