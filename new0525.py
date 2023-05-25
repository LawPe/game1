import random 
die0 = random.randint(1,9) 
die1 = random.randint(1,9) 
die2 = random.randint(1,9) 
print('Die 0 =',die0) 
print('Die 1 -',die1) 
print('Die 2 =',die2) 
if die0 == die1 and die1 == die2 and die0 == die2: 
 print('Bingo') 
elif die0 == die1 or die1 == die2 or die0 == die2: 
 print('2 equal digits') 
else: 
 print('3 different digits')
