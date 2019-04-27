import time
import random


class Generator:
    def __init__(self):
        self.nouns = open('words/nouns.txt', 'r').readlines()
        self.verbs = open('words/verbs.txt', 'r').readlines()
        self.adjectives = open('words/adjectives.txt', 'r').readlines()

    def generate_status(self):
        pattern = "It's {time} o'clock. Let's {verb} the {adjective} {noun}!"
        local_time = time.localtime().strftime('%H:%M')
        noun = self.nouns[random.randint(len(self.nouns))]
        verb = self.verbs[random.randint(len(self.verbs))]
        adjective = self.adjectives[random.randint(len(self.adjectives))]

        status = pattern.format(local_time, verb, adjective, noun)

        return status
