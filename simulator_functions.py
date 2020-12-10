import random

from map import Map
from task import Task
from crewmate import Crewmate, Impostor

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
    random.shuffle(COLORS)
    return [Crewmate((random.randint(0, size - 1), random.randint(0, size - 1)),
                     random.choices(crew_tasks, k=4), COLORS.pop()) for i in range(int(size * 1.5))]



