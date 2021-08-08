print("Hello, are you the light or dark side? Here is a quiz to decide")
L = Light = 0
D = Dark = 0
import time
print("Are you ready?(y/n)")
answer = input()
if answer == 'Y' or answer == 'Yes' or answer == 'yes'or answer == 'y':
  print ('Great, lets move onto the first question.')
else:
  print ('That is fine, take your time! We will wait 10 seconds until we start the questions.')
  time.sleep(10)
#Starting questions

LightDark1 = input('Do you perfer the Dark side or the Light side? L/D')
if LightDark1 == "L":
	Light += 1
else:
	Dark += 1
print("Light = " + str(Light) + " Dark = " + str(Dark))

#Question number 2
LightDark1 = input('Would you work with Lord Sideous or Obi Wan Kenobi? S/K')
if LightDark1 == "K":
	Light += 1
else:
	Dark += 1

#Question number 3
LightDark1 = input('Would you work with Darth Vader or Luke Skywalker? D/L')
if LightDark1 == "L":
	Light += 1
else:
	Dark += 1

#Question number 4
LightDark1 = input('Would you work with Kylo Ren or Rey Skywalker? K/R')
if LightDark1 == "R":
	Light += 1
else:
	Dark += 1

#Question number 5
LightDark1 = input('Which color do you like more? Blue, Purple, Green, or Red? B/R/G/P')
if LightDark1 == "B":
	Light += 1
elif LightDark1 == "G":
  Light += 1
elif LightDark1 == "P":
  Light += 1
else:
	Dark += 1
print("Light = " + str(Light) + " Dark = " + str(Dark))
