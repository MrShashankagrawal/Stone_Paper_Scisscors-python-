from operator import truediv
import random
def spx(comp,mine):
  if(comp==mine):
    return None
  if(comp=='s' and mine=='p'):
    return True
  if(comp=='p' and mine=='x'):
    return True
  if(comp=='x' and mine=='s'):
    return True
  else:
    return False

choice = ('s','p','x')
comp = random.randint(0,2)
comp = choice[comp]
mine = input('''S for stone
P for paper 
X for Scissors: ''' )

win = spx(comp,mine)
print(f"you chose {mine} and the computer chose {comp}")
if win is None:
  print("Match Drawn")
if win:
  print("You Won")
if win is False:
  print("You Lose")
  