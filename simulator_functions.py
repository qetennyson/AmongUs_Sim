import random

from map import Map
from task import Task
from crewmate import Crewmate

COLORS = [
    'Blue',
    'Orange',
    'Cyan',
    'Yellow',
    'Purple',
    'Green',
    'Lime',
    'Black',
    'White',
    'Pink',
    'Brown',
]

TASKS = [
    'Align Engine Output',
    'Align Telescope',
    'Assemble Artifact',
    'Buy Beverage',
    'Calibrate Distributor',
    'Chart Course',
    'Clean O2 Filter',
    'Divert Power',
    'Empty Garbage',
    'Fill Canisters',
    'Measure Weather',
    'Monitor Tree',
    'Prime Shields',
    'Process Data',
    'Record Temperature',
    'Repair Drill',
    'Sort Samples',
    'Stabilize Steering',
    'Store Artifacts',
    'Unlock Manifolds',
    'Upload Data',
]


def start_game(board_size):
    new_map = Map(board_size)
    new_map.draw_map()
    return new_map


def generate_tasks(size, num_tasks=10):
    return [Task(random.choice(TASKS), (random.randint(0, size - 1), random.randint(0, size - 1))) for i in
            range(num_tasks)]


def generate_crew(size, crew_tasks):
    """
    Creates a crew based on the size of the board, and the available tasks for the crew.
    One crewmember will be designated as the Impostor after the crew is created.

    :param size: the size of the map given as an integer (n*2 size board)
    :param crew_tasks: available tasks generated
    :return: a list of Crew() instances, one of which is set as the impostor.
    """

    random.shuffle(COLORS)
    crew = []
    existing_coords = set()

    # Uses a set to ensure no duplicate coordinates are given (might abstract this for use in movement)
    while len(existing_coords) < size * 1.5:
        crew_row = random.randint(0, size - 1)
        crew_column = random.randint(0, size - 1)
        crew_coords = (crew_row, crew_column)
        if crew_coords not in existing_coords:
            crew.append(Crewmate((crew_row, crew_column), random.choices(crew_tasks, k=4), COLORS.pop()))
            existing_coords.add(crew_coords)

    random.choice(crew).impostor = True

    for mate in crew:
        mate.set_name()

    return crew

def movement(crew, map_size):
    i = 0
    existing_coords = set()

    while len(existing_coords) < map_size * 1.5:
        crew_row = random.randint(0, map_size - 1)
        crew_column = random.randint(0, map_size - 1)
        crew_coords = (crew_row, crew_column)
        crewmate = crew[i]

        if crew_coords not in existing_coords:
            crewmate.position = (crew_row, crew_column)
            existing_coords.add(crew_coords)
            i += 1


