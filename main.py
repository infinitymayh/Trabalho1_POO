import sys
from objects import *

help_message = ("\n \nUsage: main.py [-h] {list,task,new} ... \n \n"
				"Manage your tasks in the command line!\n \n"
				"Options: -h, --help  show this help message and exit\n \n"
				"Commands: {list,task,new}\n \n")

if len(sys.argv) <= 1:
	print("Command line task manager. \nRun with -h for help.")

else:
	if sys.argv[1] == "-h" or sys.argv[1] == "--help":
		print(help_message)
		exit()
	
	elif sys.argv[1] == "list":
		if len(sys.argv) == 2:
			print("list of pending tasks")
		
		else:
			if sys.argv[2] == "-h" or sys.argv[2] == "--help":
				print("\n \nUsage: todo.py list [-h] [-a] [-p {1,2,3}]\n \n"
					"List the tasks\n \n"
					"Options:\n"
					"  -h, --help                     Show this help message and exit\n"
					"  -a, --all                      List all tasks, not only pendent\n"
					"  -p {1,2,3}, --priority {1,2,3} Show tasks with a given prioriy\n \n")
				exit()
			
			elif sys.argv[2] == "-a" or sys.argv[2] == "--all":
				print("list of all")
			
			elif sys.argv[2] == "-p" or sys.argv[2] == "--priority":
				print("list of priorities")
