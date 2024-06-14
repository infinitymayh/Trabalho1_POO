from datetime import datetime

# class =====================================================================

class task:
	def __init__(self,n_id, description):
		self._id = n_id
		self._description = description
		self._state = "pending"
		self._priority = "2"
		self._date = ""
	
	def priority(self, p=None):
		if p != None:
			self._priority = p
		return self._priority
		
	def id(self, i=None):
		if i != None:
			self._id = i
		return self._id
	
	def description(self, d=None):
		if d != None:
			self._description = d
		return self._description
	
	def state(self, s=None):
		if s != None:
			self._state = s
		return self._state
		
	def date(self, dt=None):
		if dt != None:
			self._date = dt
		return self._date


# list messages ======================================================================

def msg_pending(arquivo):
	list_message = ["Task list:\n"
				"================================================================================\n"
				"   ID Description                                      State     Pri. Date      \n",
				"--------------------------------------------------------------------------------\n"
				"================================================================================\n"]
	
	task_list = load_tasks(arquivo)
	if len(task_list)==0:
		print(list_message[0],list_message[1])
	else:
		print(list_message[0])
		for task in task_list:
			if task.state() == "pending":
				print((4-len(str(task.id())))*" ",task.id(),task.description()[:47],(47-len(task.description()))*" ",task.state(),(9-len(task.state()))*" ",task.priority()," ",task.date())
		print(list_message[1])
		
def msg_all(arquivo):
	list_message = ["Task list:\n"
				"================================================================================\n"
				"   ID Description                                      State     Pri. Date      \n",
				"--------------------------------------------------------------------------------\n"
				"================================================================================\n"]
	
	task_list = load_tasks(arquivo)
	if len(task_list)==0:
		print(list_message[0],"\n \n", list_message[1])
	else:
		print(list_message[0])
		for task in task_list:
			print((4-len(str(task.id())))*" ",task.id(),task.description()[:47],(47-len(task.description()))*" ",task.state(),(9-len(task.state()))*" ",task.priority()," ",task.date())
		print(list_message[1])
	
def msg_by_priority(arquivo, p):
	list_message = ["Task list:\n"
				"================================================================================\n"
				"   ID Description                                      State     Pri. Date      \n",
				"--------------------------------------------------------------------------------\n"
				"================================================================================\n"]
	
	task_list = load_tasks(arquivo)
	if len(task_list)==0:
		print(list_message[0],"\n \n", list_message[1])
	else:
		print(list_message[0])
		for task in task_list:
			if task.priority() == p:
				print((4-len(str(task.id())))*" ",task.id(),task.description()[:47],(47-len(task.description()))*" ",task.state(),(9-len(task.state()))*" ",task.priority()," ",task.date())
		print(list_message[1])
		
# task messages ====================================================================================
		
def show_task(arquivo, task_id):
	task_list = load_tasks(arquivo)
	for tasks in task_list:
		if tasks.id() == task_id:
			print(f"\nTask {task_id}: {tasks.description()}\nState: {tasks.state()}\nPriority: {tasks.priority()}")
			
def new_state(arquivo, task_id, state):
	with open(arquivo,'rb') as a:
			loaded_dic = pickle.load(a)
			for tasks in loaded_dic["tasks_obj"]:
				if tasks.id() == task_id:
					tasks.state(state)
	with open(arquivo, "wb") as a:
		pickle.dump(loaded_dic, a)
		
def remove_task(arquivo, task_id):
	with open(arquivo,'rb') as a:
			loaded_dic = pickle.load(a)
			for tasks in loaded_dic["tasks_obj"]:
				if tasks.id() == task_id:
					loaded_dic["tasks_obj"].remove(tasks)
	with open(arquivo, "wb") as a:
		pickle.dump(loaded_dic, a)
		
def new_priority(arquivo, task_id, priority):
	with open(arquivo,'rb') as a:
			loaded_dic = pickle.load(a)
			for tasks in loaded_dic["tasks_obj"]:
				if tasks.id() == task_id:
					tasks.priority(priority)
	with open(arquivo, "wb") as a:
		pickle.dump(loaded_dic, a)

def set_date(arquivo, task_id, date):
	
	date_time = datetime.strptime(date, "%Y-%m-%d")
	date = date_time.date()
	with open(arquivo,'rb') as a:
			loaded_dic = pickle.load(a)
			for tasks in loaded_dic["tasks_obj"]:
				if tasks.id() == task_id:
					tasks.date(date)
	with open(arquivo, "wb") as a:
		pickle.dump(loaded_dic, a)
	
	
#=================================================================================================================

# salvar as tarefas

import pickle

#nome do arquivo das tarefas

arq = "task_list.pkl"

# funcao para abrir o arquvivo das tarefas

def load_tasks(arquivo):
	try:
		with open(arquivo,'rb') as a:
			loaded_dic = pickle.load(a)
			return loaded_dic["tasks_obj"]
	except FileNotFoundError:
		return []
        
#funcao para salvar as tarefas no arquivo

def save_task(arquivo, description):
	try:
		with open(arquivo,'rb') as a:
			loaded_dic = pickle.load(a)
		
		task_id = max(loaded_dic["id"])+1
		new_task = task(task_id, description)
		loaded_dic["tasks_obj"].append(new_task)
		loaded_dic["id"].append(task_id)
		
		
		with open(arquivo,'wb') as a:
			pickle.dump(loaded_dic, a)
			
	except FileNotFoundError:
		new_task = task(1, description)
		initial_task_list = [new_task]
		initial_id_list = [1]
		
		task_dic = {
			"tasks_obj": initial_task_list,
			"id": initial_id_list
		}
		
		with open(arquivo, 'wb') as a:
			pickle.dump(task_dic, a)
	
        

