class Map:
    def __init__(self, size):
        self.size = size
        self.total_complete_tasks = 0
        self.board = [[Node(), Node(), Node(), Node()] for i in range(self.size)]

    def create_map(self):
        """
        Creates a map of empty nodes based on the given size.
        :return: multidimensional list of nodes.
        """
        pass

    def update_map(self, map, crew):
        # TODO: Extremely busted.
        for mate in crew:
            mate_y_coord, mate_x_coord = mate.position
            updating_node = map[mate_y_coord][mate_x_coord]
            updating_node.occupant = 'Crewmate'

    def draw_map(self):
        """
        Displays the map to the console.
        :return: None
        """
        print()
        for row in self.board:
            print(row)

    def place_tasks(self, tasks):
        # TODO: Removing tasks from map itself and just ticking them off from crewmate data for now.
        """
        Places tasks randomly across the map.

        :param tasks: A list of Task instances that will be assigned to random nodes on the current map.
        :return: None
        """
        # for task in tasks:
        #     y_coord = task.location[0]
        #     x_coord = task.location[1]
        #     random_node = self.board[y_coord][x_coord]
        #
        #     random_node.tasks.append(task)
        #
        #     # TODO: Doesn't seem right that coordinates are cross-dependent in this way.
        #     random_node.coordinates = task.location


class Node:
    """
    A node is used to contain data for a given space on the map.
    """

    def __init__(self, coordinates=(), occupant=None):

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
