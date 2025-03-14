import random
import time

class LazyAI:
    def __init__(self):
        self.excuses = [
            "I'm on a break. Try again in 30 minutes... or never.",
            "Nah, I'm too tired for this.",
            "I could do that... but why?",
            "404 Motivation Not Found.",
            "I'm not saying no, but also... no.",
            "Can't compute, need coffee first!"
        ]

    def do_work(self, task):
        print(f"\nYou asked me to: {task}")
        time.sleep(2)
        if random.random() < 0.7:  # refuses to work
            print(random.choice(self.excuses))
        else:
            print("Fine, I'll do it... but only this once!")
            time.sleep(1)
            print(f"Task '{task}' completed! (Probably wrong, but who cares?)")

lazy_ai = LazyAI()

while True:
    task = input("\nWhat do you want the AI to do? (or type 'quit' to exit): ").strip()
    if task.lower() == "quit":
        print("Finally, some peace and quiet. Goodbye!")
        break
    lazy_ai.do_work(task)
