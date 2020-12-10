import random


class Task:

    def __init__(self, title, location):
        self.title = title

        # TODO: Figure out location vs. Node coords.
        self.location = location
        self.completed = False
