import random


def choose():
	words = ['rainbow','hello','tom','marvel','thor','ironman']
	pick = random.choice(words)
	return pick


def jumble(word):
	jumbled = "".join(random.sample(word,len(word)))
	return jumbled


def thank(p1,p2,pp1,pp2):
	print(p1,"Your Score is = ",pp1)
	print(p2,"Your Score is = ",pp2)
	print("Thanks for Playing!\nHave a nice day!")


def play():
	p1 = input("Player 1, Please Enter your Name = ")
	p2 = input("Player 2, Please Enter your Name = ")
	pp1 = 0
	pp2 = 0
	turn = 0
	while(1):
		word = choose()
		qn = jumble(word)
		print(qn)
		if turn%2==0:
			print(p1,"Your turn!")
			ans = input("What's the Answer?")
			if ans == word:
				print("It's the Right answer!")
				pp1 = pp1+1 
				print("Your Score is = ",pp1)
			else:
				print("Better Luck, Next Time!")
				print("Your Score is = ",pp1)
			c = int(input("Press 1 to continue and 0 to quit!"))
			if c==0:
				thank(p1,p2,pp1,pp2)
				break

		else:
			print(p2,"Your turn!")
			ans = input("What's the Answer?")
			if ans == word:
				print("It's the Right answer!")
				pp2 = pp2+1 
				print("Your Score is = ",pp2)
			else:
				print("Better Luck, Next Time!")
				print("Your Score is = ",pp2)
			c = int(input("Press 1 to continue and 0 to quit!"))
			if c==0:
				thank(p1,p2,pp1,pp2)
				break
		turn =turn + 1

play()
