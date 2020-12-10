import simulator_functions as sim_f

MAP_SIZE = 4


def main():
    # Creates and Draws a New Map
    game_map = sim_f.start_game(MAP_SIZE)

    # Generates a list of tasks with titles and coordinates.
    task_list = sim_f.generate_tasks(MAP_SIZE)

    # Places the tasks in map, creating instances of Nodes
    game_map.place_tasks(task_list)

    # Generate Crew
    new_crew = sim_f.generate_crew(MAP_SIZE, task_list)
    print(new_crew)

    # Redraw Map
    game_map.update_map(new_crew)
    game_map.draw_map()


if __name__ == '__main__':
    main()
