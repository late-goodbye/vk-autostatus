import time
import random


class Generator:
    def __init__(self):
        self.nouns = open('words/nouns.txt', 'r').readlines()
        self.verbs = open('words/verbs.txt', 'r').readlines()
        self.adjectives = open('words/adjectives.txt', 'r').readlines()

    def generate_status(self):
        pattern = "It's {local_time} o'clock. Let's {verb} the {adjective} {noun}!"
        local_time = time.strftime('%H:%M', time.localtime())
        noun = self.nouns[random.randint(0, len(self.nouns))].strip()
        verb = self.verbs[random.randint(0, len(self.verbs))].strip()
        adjective = self.adjectives[random.randint(0, len(self.adjectives))].strip()

        status = pattern.format(local_time=local_time, verb=verb, adjective=adjective, noun=noun)

        time.sleep(1)
        return status