class Crewmate:

    def __init__(self, position, tasks, color):
        self.color = color
        self.position = position
        self.tasks = tasks
        self.sus_level = 0
        self.witness = False
        self.alive = True
        self.votes = 0
        self.impostor = False
        self.name = 'Crewmate'

    def set_name(self):
        if self.impostor:
            self.name = 'Impostor'

    def complete_task(self):
        pass

    def vote(self):
        pass

    def __repr__(self):
        if not self.impostor:
            return f'{self.color} Crewmate at: {self.position}'
        else:
            return f'{self.color} Impostor at: {self.position}'

