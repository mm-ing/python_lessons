import time
import random
from threading import Event

# *** section worker events
class WorkerEvents:
    def __init__(self):
        self.start_worker_event = Event()
        self.stop_worker_event = Event()

    def start_worker(self):
        self.start_worker_event.set()

    def stop_worker(self):
        self.stop_worker_event.set()


# spinner class
class Spinner:
  def __init__(self):
    self._credit = 10

    self.shutdown = False

    self.workers = {}

    self._slot = []
    
    self.actionText = [
      "Try your luck!",
      "Wheel is spinning, good luck!",
      "Try your luck again!",
      "You don't have enough credit to play!  Please restart the game!"]
    
    self._message = self.actionText[0]

    for x in range(3):
      self._slot.append(random.randint(0, 9))

  def setInitialValues(self):
      for x in range(3):
        self._slot[x] =random.randint(0, 9)

  def add_worker(self, name):
      self.workers[name] = WorkerEvents()

  def stop_workers(self):
      for worker in self.workers.values():
          worker.stop_worker()  
          worker.start_worker()

  def update_slots(self):
    pass

  def update_message(self):
    pass

  def update_credit(self):
    pass
    
  @property
  def slots(self):
      return self._slot
  
  @slots.setter
  def slots(self, value, notify=True):
      self._slot = value
      if notify:
          self.update_slots()

  @property
  def credit(self):
      return self._credit
  
  @credit.setter
  def credit(self, value, notify=True):
      self._credit = value
      if notify:
          self.update_credit()
  
  @property
  def message(self):
     return self._message
  
  @message.setter
  def message(self, value, notify=True):
      self._message = value
      if notify:
          self.update_message()
     

  def calculateResultMessage(self):
    if self._slot[0] == 7 and self._slot[1] == 7 and self._slot[2] == 7:
      reward = 10
      self.credit += reward
      return f'Concratulation, lucky No 7, you won {reward} credits!\n' + self.actionText[2]
    if self._slot[0] == self._slot[1] and self._slot[1] == self._slot[2]:
      reward = 5
      self.credit += reward
      return f'Concratulation, you won {reward} credits!\n' + self.actionText[2]
    if self._slot[0] == self._slot[1] or self._slot[1] == self._slot[2] or self._slot[0] == self._slot[2]:
      return f'Concratulation, you won your bet!\n' + self.actionText[2]
    self.credit -= 1
    return 'You lost your bet\n' + self.actionText[2]
  