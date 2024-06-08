# -> imports
import sys
from objects import *

# -> variáveis
help_message = ("\n \nUsage: main.py [-h] {list,task,new} ... \n \n"
				"Manage your tasks in the command line!\n \n"
				"Options: -h, --help  show this help message and exit\n \n"
				"Commands: {list,task,new}\n \n")
				
list_help = ("\n \nUsage: todo.py list [-h] [-a] [-p {1,2,3}]\n \n"
			"List the tasks\n \n"
			"Options:\n"
			"  -h, --help                     Show this help message and exit\n"
			"  -a, --all                      List all tasks, not only pendent\n"
			"  -p {1,2,3}, --priority {1,2,3} Show tasks with a given prioriy\n \n")
list_help2 = ("./todo.py new -h usage: todo.py new [-h] description"
			"\nCreate a task"
			"\npositional arguments: description Create a new task"
			"\noptions: -h, --help show this help message and exit")





tasklist = task_list()
tasksid = 0

# -> verifica se foi executado apenas o "main.py", nesse caso é mandada
#uma mensagem de inicialização

if len(sys.argv) <= 1:
	print("Command line task manager. \nRun with -h for help.")

# -> código principal

else:
	
	# > comando help <
	
	if sys.argv[1] == "-h" or sys.argv[1] == "--help":
		print(help_message)
		exit()
	
	# > comando list <
	
	elif sys.argv[1] == "list":
		if len(sys.argv) == 2:
			print(tasklist.msg_pending())
		
		else:
			if sys.argv[2] == "-h" or sys.argv[2] == "--help":
				print(list_help)
				exit()
			
			elif sys.argv[2] == "-a" or sys.argv[2] == "--all":
				print("list of all")
			
			elif sys.argv[2] == "-p" or sys.argv[2] == "--priority":
				print("list of priorities")
				
	# > comando new <
				
	elif sys.argv[1] == "new":
		
		if sys.argv[2] == "-h" or sys.argv[2] == "--help":
				print(list_help2)
				
			
