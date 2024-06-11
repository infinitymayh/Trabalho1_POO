class task:
	def __init__(self,n_id, description):
		self._id = n_id
		self._description = description
		self._state = "pending"
		self._priority = "2"
	
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


# list messages ======================================================================

def msg_pending(arquivo):
	list_message = ["Task list:\n"
				"================================================================================\n"
				"   ID Description                                      State     Pri. Date      \n",
				"\n--------------------------------------------------------------------------------\n"
				"================================================================================\n"]
	
	task_list = load_tasks(arquivo)
	if len(task_list)==0:
		print(list_message[0],"\n \n", list_message[1])
	else:
		print(list_message[0])
		for task in task_list:
			if task.state() == "pending":
				print("  ",task.id(),task.description(),(48-len(task.description()))*" ",task.state(),"  ",task.priority())
		print(list_message[1])
	
	
		
		
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
	
        

