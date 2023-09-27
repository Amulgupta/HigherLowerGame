# Import modules
import random
from art import logo, vs
from game_data import data

# print logo
print(logo)
# Initialize two dictionaries A and B.
A = {}
B = {}
final_score = 0

# Take random choice.
def random_personality():
  """Pick a random personality from list of personalities of game data."""
  return random.choice(data)

# Compare number of followers of both personalities
def follower(dict1, dict2):
  """Compare the number of followers of the two given personality"""
  if dict1['follower_count'] > dict2['follower_count']:
    return dict1
  return dict2

# Compare guess and dictionaries.
def plyr_choice(guess, dict1, dict2):
  """Take the option selected by user and compare it against dictionaries"""
  if guess == "A":
    return dict1
  elif guess == "B":
    return dict2
  return None

def score():
  """Calculates the score of the player in the game"""
  point = 0
  if follower(A, B) == plyr_choice(guess, A, B):
    # Even though if option is not A or B plyr_choice will contain the function return
    
    return point + 1        #[Another way was using global score then score += 1 ]
  return point
    

# Ask for option A or B
# Game continues until incorrect stop the game.
A = random_personality()
end = False
while not end:
  
  # print A
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")

  # print vs
  print(vs)
  
  B = random_personality()
  # print B
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

  # Taking input from user and coverting to uppercase.
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  follower(A, B)
  plyr_choice(guess, A, B)
  print(logo)
  # If correct guess then score increase by 1 dictionary B becomes A
  if follower(A, B) == plyr_choice(guess, A, B):
    A = B
    final_score += score()
    print(f"You're right! Current score: {final_score}.")
  else:
    end = True
    print(f"Sorry, that's wrong. Final score: {final_score}")
