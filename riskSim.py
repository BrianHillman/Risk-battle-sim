import random
import math

choice = input("1 = chance of victory \n2 = face-off\n")
def roll(dsa = 0):
	return random.randrange(1,7)
	
	
if choice == 2:
	defe = input("defenders: ")
	att = input("attackers: ")

	while att > 1 and defe > 0:
		attackRolls = sorted([roll(x) for x in range(min(3,att-1))], reverse = True)
		defRolls = sorted([roll(x) for x in range(min(2,defe))], reverse = True)
		for x in range(min(len(defRolls),len(attackRolls))):
			if defRolls[(x)] < attackRolls[(x)]:
				defe -= 1
			else:
				att -= 1 
	print "attackers remaining : ",att,"\ndefenders remaining : ",defe
	pause = input("press ENTER to exit.")
	
else:
	defe1 = input("defenders: ")
	att1 = input("attackers: ")
	trials = input("trials")
	wins = 0
	for x in xrange(trials):
		att = att1
		defe = defe1
		while att > 1 and defe > 0:
				attackRolls = sorted([roll(x) for x in range(min(3,att-1))], reverse = True)
				defRolls = sorted([roll(x) for x in range(min(2,defe))], reverse = True)
				for x in range(min(len(defRolls),len(attackRolls))):
					if defRolls[(x)] < attackRolls[(x)]:
						defe -= 1
					else:
						att -= 1 
		if att > 1:
			wins += 1
	print 100.0*wins/trials,"%"
	pause = input("press ENTER to exit.")