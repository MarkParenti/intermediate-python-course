import random


def main():
  dice_sum = 0
  
  dice_rolls = int(input("How many dice would you like to roll?"))
  sides = int(input("How many sides should the die have?"))


  for i in range(0, dice_rolls):
    roll = random.randint(1,sides)
    if roll == 1:
      print(f'You rolled a {roll}! Critical Fail')
    elif roll == sides:
      print(f'You rolled a {roll}! Critical Success!')
    else:
       print(f'You rolled a {roll}')
    dice_sum = dice_sum + roll
 

  if dice_rolls != 1:
    print(f"Your total is {dice_sum}!")

if __name__== "__main__":
  main()