class Crewmate:
    #TODO: Don't think inheritance actually makes sense and impostor should just be a Boolean.
    def __init__(self, position, tasks, color):
        self.color = color
        self.position = position
        self.tasks = tasks
        self.sus_level = 0
        self.witness = False
        self.alive = True
        self.votes = 0

    def move(self):
        pass

    def complete_task(self):
        pass

    def vote(self):
        pass

    def __repr__(self):
        return f'{self.color} Crewmate at: {self.position}'


class Impostor(Crewmate):

    def __init__(self, color, position, tasks):
        super(Impostor, self).__init__(color, position, tasks)

        self.kills = 0
        # TODO: Adjacencies is inherited?
        self.adjacencies = 0
