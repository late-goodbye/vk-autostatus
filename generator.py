import time
import random
import os


class Generator:
    def __init__(self):
        self.nouns = open('words/nouns.txt', 'r').readlines()
        self.verbs = open('words/verbs.txt', 'r').readlines()
        self.adjectives = open('words/adjectives.txt', 'r').readlines()
        self.emojies = open('words/emojies.txt', 'r').readlines()
        self.token = os.environ.get('token')
        time.tzset()

    def generate_status(self):
        pattern = "It's {local_time} o'clock. Let's {verb} the {adjective} {noun}{emoji}"
        local_time = time.strftime('%H:%M', time.localtime())
        noun = self.nouns[random.randint(0, len(self.nouns))].strip()
        verb = self.verbs[random.randint(0, len(self.verbs))].strip()
        adjective = self.adjectives[random.randint(0, len(self.adjectives))].strip()
        emojie = self.emojies[random.randint(0, len(self.emojies))].strip()

        status = pattern.format(local_time=local_time,
                                verb=verb,
                                adjective=adjective,
                                noun=noun,
                                emojie=emojie)
        return status
