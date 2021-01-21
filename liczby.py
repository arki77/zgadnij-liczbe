import random
import os


def tryb():
	os.system("cls")
	print('Ilu cyfrowa ma byc liczba?')
	dlugosc = int(input())
	x = '1' + '0' * (dlugosc-1)
	y = '9' * dlugosc
	liczba = random.randint(int(x), int(y))
	return liczba
	
def gra():
	zgadywana = tryb()
	hacktry = 0
	while True:
		print(f'Zgadnij liczbe {len(str(zgadywana))} cyfrowa!')
		hack = int(input(''))
		if zgadywana > hack:
			print('Liczba jest za małą!')
			hacktry = hacktry + 1
		elif zgadywana < hack:
			print('Liczba jest za duża!')
			hacktry = hacktry + 1
		elif zgadywana == hack:
			hacktry = hacktry + 1
			os.system("cls")
			print('Gratulacje!! Udało Ci się!')
			print(f'Zajeło Ci to {hacktry} prób!')
			finish = input('Wcisnij enter aby zagrać jeszcze raz!')
			gra()

gra()

