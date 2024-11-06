import random
random_number = random.randint(1, 100)

def searchForSpecificNumber(guess):
  if random_number == guess:
    print("Perfecto")
  elif guess > random_number:
    print("To hi")
  elif guess < random_number:
    print("To low")
  
print("Welcome to the Number Guessing Game! \n I am thinking of a number between 1 and 100.")
user_Level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
user_lifes = 0


if user_Level == 'hard':
  user_lifes = 5
  print("You have 5 attempts remaining to guess the number.")
elif user_Level == 'easy':
  user_lifes = 10
  print("You have 10 attempts remaining to guess the number.")

while user_lifes > 0:
  user_number = int(input("Make a guess: "))
  searchForSpecificNumber(user_number)

