import random
print("Welcome to the Rock, Paper & Scissors Game!!!".upper())
while True:
  choices = ["rock","paper", "scissors"]
  computer = random.choice(choices)
  player = None
  while player not in choices:
   player = input(str("what's your choice? \n")).lower()

  print("computer: ",computer)
  print("Player: ", player)
  if player == computer:
    print ("It is a tie, Play again! ")
  elif player == "rock":
    if computer == "scissors":

     print("You win!")
    if computer == "paper":

     print("You Lose! Try again")
  elif player == "scissors":
    if computer == "paper":

     print("You win!")
    if computer == "rock":

     print("You Lose! Try again")
  elif player == "paper":
    if computer == "rock":

     print("You win!")
    if computer == "scissors":

     print("You Lose! Try again")
  try_again = input("do you want to play again? Y/N\n")
  if try_again!= "Y":
   break
print("Hope you enjoyed the game?"
      "have a nice day!")