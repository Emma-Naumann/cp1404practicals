"""
Emma Naumann
CP1404 Practical 7
Do from scratch exercises - project management program

Estimate: 1 hour
Actual:
"""
import datetime
from prac_07.project import Project

MENU = "- (L)oad projects \n- (S)ave projects \n- (D)isplay projects \n- (F)ilter projects by date" \
       "\n- (A)dd new project \n- (U)pdate project \n- (Q)uit \n>>> "


def main():
    """Load and save a data file and use a list of Project objects."""
    choice = input(MENU).upper()
    # if user doesn't choose load first, automatically load projects.txt
    projects = load_projects("projects.txt")
    incomplete_projects = []
    complete_projects = []
    while choice != "Q":
        for project in projects:
            if project.completion_percentage == "100" and project not in complete_projects:
                complete_projects.append(project)
            elif project.completion_percentage != "100" and project not in incomplete_projects:
                incomplete_projects.append(project)
        incomplete_projects.sort()
        complete_projects.sort()
        if choice == "L":
            # update loaded projects if user chooses different file
            file_to_load = input("Filename: ")
            projects = load_projects(file_to_load)
        elif choice == "S":
            save_project(projects)
        elif choice == "D":
            display_projects(incomplete_projects, complete_projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        choice = input(MENU).upper()
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from user file and store in a nested list."""
    projects = []
    with open(filename) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            new_project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), parts[4])
            projects.append(new_project)
    return projects


def save_project(projects):
    file_to_save = input("Filename: ")
    with open(file_to_save, "w") as out_file:
        for project in projects:
            print(project, file=out_file)


def display_projects(incomplete_projects, complete_projects):
    """Display formatted projects."""
    print(f"Incomplete projects:")
    for project in incomplete_projects:
        print(f"\t {project}")
    print(f"Complete projects:")
    for project in complete_projects:
        print(f"\t {project}")


def filter_projects(projects):
    """Filter projects by date and display sorted projects that start after that date."""
    filter_date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(filter_date_string, "%d/%m/%Y").date()
    filtered_projects = []
    for project in projects:
        if project.start_date >= filter_date:
            filtered_projects.append(project)
    filtered_projects.sort()
    for project in filtered_projects:
        print(project)


def add_project(projects):
    """Add new project to projects after error-checking user input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion_percentage = input("Percent complete: ")
    new_project = Project(name, start_date, priority, cost, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Prompt user to update a project completion percentage and priority by number (error-checked)."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    is_valid_project_index = False
    while not is_valid_project_index:
        try:
            project_to_update_index = int(input("Project choice: "))
            if project_to_update_index < 1:
                print("Number must be >= 1")
            elif project_to_update_index > len(projects):
                print("Invalid project number")
            else:
                print(projects[project_to_update_index])
                is_valid_project_index = True
        except ValueError:
            print("Invalid input; enter a valid number")
    is_valid_percentage = False
    while not is_valid_percentage:
        try:
            new_percentage = int(input("New Percentage: "))
            if new_percentage < 1 or new_percentage > 100:
                print("Percentage must be >= 1 and <= 100")
            elif new_percentage == "":
                is_valid_percentage = True
            else:
                # safe to ignore reference warning
                # TODO: update project with new_percentage and priority
                Project(project_to_update_index).completion_percentage = new_percentage
                # chosen_project = projects[project_to_update_index]
                # chosen_project.completion_percentage(int(new_percentage))
                # print(chosen_project)
                # print(projects[project_to_update_index])
                is_valid_percentage = True
        except ValueError:
            print("Invalid input; enter a valid number")
    is_valid_priority = False
    while not is_valid_priority:
        try:
            new_priority = int(input("New Priority: "))
            if new_priority < 1:
                print("Percentage must be >= 1")
            elif new_priority == "":
                is_valid_priority = True
            else:
                # safe to ignore reference warning
                # projects[project_to_update_index][2] = new_priority
                is_valid_priority = True
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == '__main__':
    main()
