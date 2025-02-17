import numpy as np

class KarmicRL:
    def __init__(self):
        self.karma_score = 0

    def take_action(self, action):
        karma_rewards = {"help": +10, "lie": -5, "steal": -20}
        self.karma_score += karma_rewards.get(action, 0)
        return self.karma_score

if __name__ == "__main__":
    ai = KarmicRL()
    print(f"Action: Help, New Karma Score: {ai.take_action('help')}")
src/karmic_rl.py
