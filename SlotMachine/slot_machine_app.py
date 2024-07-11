from slot_machine_ui import GUI
from slot_machine_data import Spinner
from slot_machine_worker import Worker


if __name__ == '__main__':

    data_model = Spinner()

    ui = GUI(data_model)

    # create a worker

    worker_name = 'slot_machine_worker'

    data_model.add_worker(worker_name)

    slot_machine_worker = Worker(data_model, worker_name)
    slot_machine_worker.start()

    # start the tkinter event loop
    ui.root.mainloop()