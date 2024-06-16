import time
import random

# slot machine rotation function
def rotate(spinner,  slotLabel):
  rotations = 3
  spinnerNo = spinner.__len__()
  countStart = 1
  slotLabel[3].configure(text = '0')
  for z in range(spinnerNo):
    for y in range(rotations):
        for x in range(countStart, spinnerNo):
            spinner[x].rotate(slotLabel[x])
    countStart += 1

# spinner class
class Spinner:
  def __init__(self):
    self.s = []
    self.actionText = [
      "Try your luck!",
      "Wheel is spinning, good luck!",
      "Try your luck again!",
      "You don't have enough credit to play!  Please restart the game!"]
    self.setCredit()
    for x in range(3):
      self.s.append(random.randint(0, 9))

  def setCredit(self):
    self.credit = 10

  def setInitialValues(self):
      for x in range(3):
        self.s[x] =random.randint(0, 9)

  def resultMessage(self):
    if self.s[0] == 7 and self.s[1] == 7 and self.s[2] == 7:
      reward = 10
      self.credit += reward
      return f'Concratulation, lucky No 7, you won {reward} credits!\n' + self.actionText[2]
    if self.s[0] == self.s[1] and self.s[1] == self.s[2]:
      reward = 5
      self.credit += reward
      return f'Concratulation, you won {reward} credits!\n' + self.actionText[2]
    if self.s[0] == self.s[1] or self.s[1] == self.s[2] or self.s[0] == self.s[2]:
      return f'Concratulation, you won your bet!\n' + self.actionText[2]
    self.credit -= 1
    return 'You lost your bet\n' + self.actionText[2]
  
  def rotate(self, slotLabel):
    start=0
    for z in range(3):
        for y in range(10):
            for x in range(start, 3):
                self.s[x] += 1
                if self.s[x] > 9: self.s[x] = 0
                slotLabel[x].configure(text = self.s[x])
                slotLabel[x].update()
                time.sleep(.05)    #Pause .1 seconds
        start+=1