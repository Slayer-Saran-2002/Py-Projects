rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_img=[rock,paper,scissors]
import random
user=int(input("Enter your choice (1:Rock , 2:Paper , 3:scissors)\n"))
if user>3 or user<0:
  print("You have entered an invalid input!")
else:
  print("You have chosen -->")
  print(game_img[user-1])
  computer = random.randint(1,3)
  print("Computer has chosen -->")
  print(game_img[computer-1])
    # Wining conditions
  if user==1 and computer==3:
    print("You Win !")
  elif user==1 and computer==2:
    print("You Lose !")
    
  elif user==2 and computer==3:
    print("You Lose !")
  elif user==2 and computer==1:
    print("You Win !")
    
  elif user==3 and computer==2:
    print("You Win !")
  elif user==3 and computer==1:
    print("You Lose !")

  else:
    print("Draw !")
    