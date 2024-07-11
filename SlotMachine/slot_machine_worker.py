from slot_machine_data import Spinner
from threading import Thread
from time import sleep


class Worker(Thread):
    def __init__(self, data_model: Spinner, name: str):
        Thread.__init__(self, daemon=True)
        self.data_model = data_model
        self.name = name

        self.worker_events = self.data_model.workers[self.name]

    def run(self):

        while self.data_model.shutdown is False:         
           
            self.worker_events.start_worker_event.wait()
            self.worker_events.start_worker_event.clear()

            if self.data_model.credit < 1:
                self.data_model.actionText = self.data_model.actionText[3]
                continue

            self.data_model.message = self.data_model.actionText[1]

            start=0
            slots = self.data_model.slots
            for z in range(3):
                for y in range(30):
                    for x in range(start, 3):
                        slots[x] += 1
                        if slots[x] > 9: slots[x] = 0
                        sleep(.02)    #Pause .05 seconds
                    self.data_model.slots = slots
                start+=1
            self.data_model.message = self.data_model.calculateResultMessage()

            if self.worker_events.stop_worker_event.is_set():
                self.worker_events.stop_worker_event.clear()
                break
                