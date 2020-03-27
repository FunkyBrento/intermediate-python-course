import random

def main():
  
  
  dice_rolls = 2
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum = dice_sum + roll
    if roll == 1:
      print(f'You suck a {roll}')
    elif roll == 6:
      print(f'you think you cool for rolling a {roll}')
    else: print(f' blah {roll}')
  print(f'yo total is {dice_sum}')
  
if __name__== "__main__":
  main()