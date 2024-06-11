# -> imports
import sys
from objects import *

# -> variáveis
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
		exit()
	
	# > comando list <
	
	elif sys.argv[1] == "list":
		if len(sys.argv) == 2:
			msg_pending()
		
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
		
		#comando de ajuda
		
		if sys.argv[2] == "-h" or sys.argv[2] == "--help":
				print(new_help)
				
		#criando uma nova tarefa
		
		else:
			nova_tarefa=sys.argv[2]
			tarefa,estado,prioridade,id_usados=carregar_tarefas(nome_arquivo)
			
			# caso não exista uma lista de tarefas
			
			if not tarefa:
				tarefas = {}
				estado = {}
				prioridade = {}
				id_usados = {}
				n_id = 0
				
			if tarefa:
				n_id=max(id_usados.values())

			# salvar tarefas no arquivo

			tarefa[n_id]=nova_tarefa
			estado[n_id]="pending"
			prioridade[n_id]=2
			id_usados[n_id] = n_id+1
			salvar_tarefas(tarefa,estado,prioridade, id_usados, nome_arquivo)
	
	# > comando task <
	
	elif sys.argv[1] == "task":
		try:
			if sys.argv[2] == "-h" or sys.argv[2] == "--help":
				print(task_help)
		except IndexError:
			print("\nErro! O comando deve ser seguido do número de identificação da tarefa.")
			
		
			

