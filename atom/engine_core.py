import time
import yaml
from scheduler import Scheduler

class EngineCore:
    def __init__(self, config_path='config.yaml'):
        self.config = self.load_config(config_path)
        self.scheduler = Scheduler()

    def load_config(self, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def execute(self, task):
        print(f"[ENGINE] Executing task: {task['name']}")
        time.sleep(task.get('duration', 1))

    def run(self):
        print("[ENGINE] Starting engine loop...")
        while True:
            task = self.scheduler.get_next_task()
            if task:
                self.execute(task)
            else:
                print("[ENGINE] No tasks available. Sleeping...")
                time.sleep(2)

if __name__ == '__main__':
    engine = EngineCore()
    engine.run()
