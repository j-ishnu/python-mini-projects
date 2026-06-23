print('🧠Welcome to the simple quiz game!\n')
questions=[
{"q":"What is the capital of France?","options":["Berlin","Paris","Madrid","Rome"],"answer":2},
{"q":"Which Planet is called as the Red Planet?","options":["Earth","Mars","Venus","Jupiter"],"answer":2},
{"q":"What is 51+211?","options":["262","155","172","123"],"answer":1}
]
import random,time
w='yes'
while w=='yes':
	time.sleep(3)
	start_time=time.time()
	c=0
	random.shuffle(questions)
	for q in questions:
		print(q["q"])
		for i in range(4):
			print(f"{i+1}.{q['options'][i]}")
		ans=int(input("Enter your answer (1-4):"))
		if ans==q["answer"]:
			print("✅Correct!\n")
			c=c+1
		else:
			print("❌Incorrect!\n")		
	print(f'You have corrected {c} out of 3🎉')
	time.sleep(2)
	if c==3:
		print('\nyou have corrected all🏆🏆')
		w='no'
		end_time=time.time()
		total_time=end_time-start_time
		print(f'You completed the quiz in {round(total_time-1)} seconds')
	elif c==0:
		end_time=time.time()
		print('\ntry again!? (yes/no):\n')
		w=input().lower()		
	else:	
		end_time=time.time()
		print('\nYou are almost there!\n Try again? (yes/no):\n')
		w=input().lower()
		



