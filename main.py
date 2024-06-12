# -> imports
import sys
from objects import *
import pickle


# -> variáveis de texto
help_message = ("\n \nUsage: main.py [-h] {list,task,new} ... \n \n"
				"Manage your tasks in the command line!\n \n"
				"Options:\n"
				 "-h, --help  show this help message and exit\n \n"
				"Commands:\n"
				"{list,task,new}\n \n")
				
list_help = ("\n \nUsage: todo.py list [-h] [-a] [-p {1,2,3}]\n \n"
			"List the tasks\n \n"
			"Options:\n"
			"  -h, --help                     Show this help message and exit\n"
			"  -a, --all                      List all tasks, not only pendent\n"
			"  -p {1,2,3}, --priority {1,2,3} Show tasks with a given prioriy\n \n")
			
new_help = ("\n\n./todo.py new -h usage: todo.py new [-h] description"
			"\n\nCreate a task"
			"\n\npositional arguments:\n  -description Create a new task"
			"\n\noptions:\n  -h, --help show this help message and exit")
			
task_help = ("\n \nUsage: todo.py task [-h] [-d | -c | -r | -s SCHEDULE | -p {1,2,3}] id\n \n"
			"Act on a task\n \n"
			"positional arguments:\n"
			"id                    Specify task id\n \n"
			"options:\n"
			"-h, --help            show this help message and exit\n"
			"-d, --done            Mark task as done\n"
			"-c, --cancelled       Mark task as cancelled\n"
			"-r, --remove          Remove task\n"
			"-s SCHEDULE, --schedule SCHEDULE\n"
			"                       Schedule the task\n"
			"-p {1,2,3}, --priority {1,2,3}\n"
			"                      Change priority level")



# -> verifica se foi executado apenas o "main.py", nesse caso é mandada
#uma mensagem de inicialização

if len(sys.argv) <= 1:
	print("Command line task manager. \nRun with -h for help.")

# -> código principal

else:
	
	
	# > comando help <
	
	if sys.argv[1] == "-h" or sys.argv[1] == "--help":
		print(help_message)
	
	# > comando list <
	
	elif sys.argv[1] == "list":
		if len(sys.argv) == 2:
			msg_pending(arq)
		
		else:
			if sys.argv[2] == "-h" or sys.argv[2] == "--help":
				print(list_help)
			
			elif sys.argv[2] == "-a" or sys.argv[2] == "--all":
				msg_all(arq)
			
			elif sys.argv[2] == "-p" or sys.argv[2] == "--priority":
				try:
					msg_by_priority(arq, sys.argv[3])
				except IndexError:
					print("\nError! The command should be followed by a priority number {1, 2, 3}. Use 'list -h' or 'list --help' for help.")
					
	# > comando new <
				
	elif sys.argv[1] == "new":
		
		try:
			
		#comando de ajuda
		
			if sys.argv[2] == "-h" or sys.argv[2] == "--help":
				print(new_help)
				
		#criando uma nova tarefa
		
			else:
				save_task(arq, sys.argv[2])
				
		except IndexError:
			print("\nError! The command should be followed by a description. Use -h or --help for help.")
			
	
	# > comando task <
	
	elif sys.argv[1] == "task":
		try:
			if sys.argv[2] == "-h" or sys.argv[2] == "--help":
				print(task_help)
				
			elif len(sys.argv) == 3:
					show_task(arq, int(sys.argv[2]))
				
			elif sys.argv[3] == "-d" or sys.argv[3] == "--done":
					new_state(arq, int(sys.argv[2]), "done")
					
			elif sys.argv[3] == "-c" or sys.argv[3] == "--cancelled":
					new_state(arq, int(sys.argv[2]), "cancelled")
				
			elif sys.argv[3] == "-r" or sys.argv[3] == "--remove":
					remove_task(arq, int(sys.argv[2]))
					
			elif sys.argv[3] == "-p" or sys.argv[3] == "--priority":
					if int(sys.argv[4]) not in range(0,4):
						raise IndexError("The priority needs to be 1, 2 or 3.")
						
					else:
						new_priority(arq, int(sys.argv[2]), sys.argv[4])
			
		except IndexError:
			raise
			print("\nError! The command should be followed by a existing task id. Use -h or --help for help.")
			
		
			

