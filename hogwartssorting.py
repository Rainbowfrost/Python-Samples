print("Hello, I'm the Hogwarts sorting hat! I will be asking you a few questions, and depending on what you answer for each one, you will be sorted to a house!")
gryffindor = 0
ravenclaw = 0
slytherin = 0 
hufflepuff = 0 
print("Are you ready?(y/n)")
answer = input()
if answer == 'Y' or answer == 'Yes' or answer == 'yes'or answer == 'y':
  print ('Great, lets move onto the first question.')
else:
  print ('That is fine, take your time!')
#Starting questions
print("here are the houses: [G]ryffindor, [R]avenclaw, [S]lytherin, or [H]ufflepuff")

q1 = input('Which house to you like more? ')

if q1 == "G":
	gryffindor += 1
elif q1 == "R":
	ravenclaw += 1
elif q1 == "S":
	slytherin += 1
else:
	hufflepuff += 1
print ("Here are the colors: [R]ed [B]lue [G]reen [Y]ellow")

q2 = input('Out of these 4 colors, which is your favorite?')
if q1 == "R":
	gryffindor += 1
elif q1 == "B":
	ravenclaw += 1
elif q1 == "G":
	slytherin += 1
else:
	hufflepuff += 1