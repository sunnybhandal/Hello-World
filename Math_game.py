# THE MATH QUESTION

def score(question):
	""" Fun function for math questions"""
	player_score = 0

	# Take input and check result
	for a, b in question:
		answer = int(input("What is " + str(a) + "+" + str(b) + "? "))
		if answer == a + b:
			print("Correct!")
			player_score += 1
		else:
			print("Sorry it was", str(a + b))

	# Determine the players grade
	print(player_score)
	if player_score == len(question):
		score = player_score/len(question)*100
		print(f"Congrats! {score}%")
	elif player_score < len(question):
		score = player_score/len(question)*100
		if player_score > (len(question) / 2):
			print(f"Not bad, you got {score}%")
		else:
			print(f"Yikes, you got {score}")
    
# Setup the questions
question = [
	[2,2],
	[3,3],
	[4,5],
	[9,0],
	[6,2]
]

# Call function
score(question)