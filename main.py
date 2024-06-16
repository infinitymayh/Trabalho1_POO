import sys
from objects import *
import pickle

# Help messages
HELP_MESSAGE = """
Usage: main.py [-h] {list,task,new} ...

Manage your tasks in the command line!

Options:
 -h, --help  show this help message and exit

Commands:
{list,task,new}
"""

LIST_HELP = """
Usage: todo.py list [-h] [-a] [-p {1,2,3}]

List the tasks

Options:
  -h, --help                     Show this help message and exit
  -a, --all                      List all tasks, not only pending
  -p {1,2,3}, --priority {1,2,3} Show tasks with a given priority
"""

NEW_HELP = """
Usage: todo.py new [-h] description

Create a task

Positional arguments:
  - description Create a new task

Options:
  -h, --help show this help message and exit
"""

TASK_HELP = """
Usage: todo.py task [-h] [-d | -c | -r | -s SCHEDULE | -p {1,2,3}] id

Act on a task

Positional arguments:
  - id Specify task id

Options:
  -h, --help            show this help message and exit
  -d, --done            Mark task as done
  -c, --cancelled       Mark task as cancelled
  -r, --remove          Remove task
  -s SCHEDULE, --schedule SCHEDULE Schedule the task
  -p {1,2,3}, --priority {1,2,3} Change priority level
"""


def print_help_message():
    print(HELP_MESSAGE)

def print_list_help():
    print(LIST_HELP)

def print_new_help():
    print(NEW_HELP)

def print_task_help():
    print(TASK_HELP)

#commands
def handle_help_command():
    if len(sys.argv) == 2: #if only "-h" show main help
        print_help_message()
    else:
        command = sys.argv[2]
        if command == "list":
            print_list_help()
        elif command == "new":
            print_new_help()
        elif command == "task":
            print_task_help()

def handle_list_command():
    if len(sys.argv) == 2: #if only "list" just show pending tasks
        msg_pending(arq)
    else:
        option = sys.argv[2]
        if option in ("-h", "--help"):
            print_list_help()
        elif option in ("-a", "--all"):
            msg_all(arq)
        elif option in ("-p", "--priority"):
            try:
                msg_by_priority(arq, sys.argv[3])
            except IndexError: #if list be followed by something different than -h, -a or -p
                print("Error! The command should be followed by a "
					"priority number {1, 2, 3}. Use 'list -h' or "
					"'list --help' for help.")

def handle_new_command():
    try:
        if sys.argv[2] in ("-h", "--help"):
            print_new_help()
        else:
            save_task(arq, sys.argv[2])
    except IndexError: #if there is nothing following new command
        print("Error! The command should be followed by a description."
			"Use -h or --help for help.")

def handle_task_command():
    try:
        if sys.argv[2] in ("-h", "--help"):
            print_task_help()
        elif len(sys.argv) == 3: #if nothing follows the id, just show task's atributes
            show_task(arq, int(sys.argv[2]))
        else:
            task_id = int(sys.argv[2])
            action = sys.argv[3]
            if action in ("-d", "--done"):
                new_state(arq, task_id, "done")
            elif action in ("-c", "--cancelled"):
                new_state(arq, task_id, "cancelled")
            elif action in ("-r", "--remove"):
                remove_task(arq, task_id)
            elif action in ("-p", "--priority"):
                try:
                    priority = int(sys.argv[4])
                    if priority not in range(1, 4): #priority can't be different than 1, 2 or 3
                        raise ValueError("The priority needs to be "
										"1, 2, or 3.")
                    new_priority(arq, task_id, priority)
                except IndexError: #if there is no priority number following "-p"
                    print("Error! The command should be followed by a "
						"priority number {1, 2, 3}. Use 'task -h' or "
						"'task --help' for help.")
            elif action in ("-s", "--schedule"):
                try:
                    set_date(arq, task_id, sys.argv[4])
                except ValueError: #the command should be followed by a date and the date needs to be on ISO format
                    print("Error! The command '-s' should be followed "
                    "by a date in format YEAR-MONTH-DAY (YYYY-MM-DD).")
			
            else:
                raise ValueError
    except IndexError: #if there is nothing following the command or the id doesn't exist
        print("Error! The command should be followed by an existing "
			"task id. Use 'task -h' or "
						"'task --help' for help.")
    except ValueError: #If command does not exist
        print(f"Error! There is no 'task {sys.argv[3]}' command. Use 'task -h' or 'task --help' for help.")


#main
def main():
	try:
		if len(sys.argv) <= 1:
			print("Command line task manager. \nRun with -h for help.")
		else:
			command = sys.argv[1]
			if command in ("-h", "--help"):
				handle_help_command()
			elif command == "list":
				handle_list_command()
			elif command == "new":
				handle_new_command()
			elif command == "task":
				handle_task_command()
			else: #if the command does not exist
				raise ValueError
	except ValueError:
		print(f"Error! There is no '{command}' command."
					" Use -h or --help for help.")

if __name__ == "__main__":
    main()
			

