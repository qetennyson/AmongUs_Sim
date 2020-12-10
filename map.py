class Map:

    def __init__(self, size):
        self.size = size
        self.total_complete_tasks = 0
        self.game_map = self.create_map()

    def create_map(self):
        """
        Creates a map of empty nodes based on the given size.
        :return: multidimensional list of nodes.
        """
        return [[Node()] * self.size for i in range(self.size)]

    def update_map(self, crew):
        # TODO: Extremely busted.
        

    def draw_map(self):
        """
        Displays the map to the console.
        :return: None
        """
        print()
        for row in self.game_map:
            print(row)

    def place_tasks(self, tasks):
        """
        Places tasks randomly across the map.

        :param tasks: A list of Task instances that will be assigned to random nodes on the current map.
        :return: None
        """
        for task in tasks:
            y_coord = task.location[0]
            x_coord = task.location[1]
            random_node = self.game_map[y_coord][x_coord]

            random_node.tasks.append(task)

            # TODO: Doesn't seem right that coordinates are cross-dependent in this way.
            random_node.coordinates = task.location


class Node:
    """
    A node is used to contain data for a given space on the map.
    """

    def __init__(self, tasks=[], coordinates=(), occupant=None):

        self.tasks = tasks
        self.coordinates = coordinates
        self.occupant = occupant

    def __repr__(self):
        if self.occupant == 'Impostor':
            return '|_X_|'
        elif self.occupant == 'Crewmate':
            return '|_O_|'
        else:
            return '|_ _|'

    def __str__(self):
        if self.occupant == 'Impostor':
            return '|_X_|'
        elif self.occupant == 'Crewmate':
            return '|_O_|'
        else:
            return '|_ _|'
