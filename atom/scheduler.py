import random

class Scheduler:
    def __init__(self):
        self.task_queue = [
            {'name': 'TaskA', 'duration': 1},
            {'name': 'TaskB', 'duration': 2},
            {'name': 'TaskC', 'duration': 1.5},
        ]

    def get_next_task(self):
        if self.task_queue:
            return self.task_queue.pop(0)
        else:
            return None
