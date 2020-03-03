import random

guessesTaken = 0

print("Hello what is your name?")
myName = input()

number = random.randint(1,20)
print("Hello, " + myName + "! I am thinking of a number between 1 and 20, you have 5 guesses to guess the correct answer. If you can guess the number correctly I will tell you my name.")

while guessesTaken < 5:
  print("Take your guess!")
  guess = input()
  if (guess.isdigit() == False):
      print("Your input was invalid.")
      validInput = False
      while (validInput == False):
          guess = input("Take your guess!")
          if (guess.isdigit() == True):
              validInput = True
  guess = int(guess)

  guessesTaken = guessesTaken + 1

  if guess < number:
    print("Your guess is low!")

  if guess > number:
    print("Your guess is high!")

  if guess == number:
    break

if guess == number:
  if guessesTaken == 1:
    print("Good job " + myName + "! You guessed my number in 1 guess! My name is Isaac Varghese, its been a pleasure playing with you!")

  else:
    print("Good job " + myName + "! You guessed my number in " +
    str(guessesTaken) + " guesses! My name is Isaac Varghese, its been a pleasure playing with you!")

if guess != number:
  number = str(number)
  print("Nope, I'm sorry, the number I was thinking of was " +
  number + ".")
