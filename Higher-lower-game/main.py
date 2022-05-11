from game_data import data 
from art import logo ,vs
import random

# generate opponents
def opponent_gen():
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

    
print(logo)
game_end = False
# assigining dictionaris
points =0
while game_end is False:
  op1=opponent_gen()
  op2=opponent_gen()
  print(format_data(op1))
  print(vs)
  print(format_data(op2))
  a_followers = op1.get("follower_count")
  b_followers = op2["follower_count"]
  winner= max(a_followers,b_followers)
  choice=input("Who has more Followers?(A/B): ").lower()
  if choice == 'a':
    user_ans= a_followers
  if choice == 'b':
    user_ans= b_followers
  if user_ans == winner:
    points+=1
    print("Nice! Try the next one")
  else:
    print(f"You failed , \nYour score is {points}")
    break
    
    
  


