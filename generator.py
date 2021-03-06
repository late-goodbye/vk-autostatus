import time
import random
import os


class Generator:
    def __init__(self):
        self.nouns = open('words/nouns.txt', 'r').readlines()
        self.verbs = open('words/verbs.txt', 'r').readlines()
        self.adjectives = open('words/adjectives.txt', 'r').readlines()
        self.token = os.environ.get('token')
        time.tzset()

    def generate_status(self):
        pattern = "It's {local_time} o'clock. Let's {verb} the {adjective} {noun}!"
        local_time = time.strftime('%H:%M', time.localtime())
        noun = self.nouns[random.randint(0, len(self.nouns) - 1)].strip()
        verb = self.verbs[random.randint(0, len(self.verbs) - 1)].strip()
        adjective = self.adjectives[random.randint(0, len(self.adjectives) - 1)].strip()

        status = pattern.format(local_time=local_time,
                                verb=verb,
                                adjective=adjective,
                                noun=noun)
        return status
