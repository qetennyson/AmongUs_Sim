import simulator_functions as sim_f

MAP_SIZE = 4


def main():
    # Creates and Draws a New Map
    new_map = sim_f.start_game(MAP_SIZE)

    # Generates a list of tasks with titles and coordinates.
    task_list = sim_f.generate_tasks(MAP_SIZE)

    # Places the tasks in map, creating instances of Nodes
    new_map.place_tasks(task_list)

    # Generate Crew
    new_crew = sim_f.generate_crew(MAP_SIZE, task_list)
    print(new_crew)

    while True:
        # Redraw Map
        new_map.update_map(new_map.board, new_crew)
        new_map.draw_map()

        # Movement
        sim_f.movement(new_crew, MAP_SIZE)


if __name__ == '__main__':
    main()
