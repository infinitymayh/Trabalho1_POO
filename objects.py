class task:
	def __init__(self, n_id, description):
		self._id = n_id
		self._description = description
		self._state = "pending"
		self.priority = 2
	
	def priority(self, p=None):
		if p != None:
			self.priority = p
		return self.priority

class task_list:
	def __init__(self):
		self._tasks = {}
		self._ids = 0
		self.list_message = ["Task list:\n"
				"================================================================================\n"
				"   ID Description                                      State     Pri. Date      \n",
				"\n--------------------------------------------------------------------------------\n"
				"================================================================================\n"]
	
	def add(self, task):
		self._tasks[ids] = task
		self._ids += 1
	
	def msg(self):
		return str(self.list_message[0]+'\n'.join(i for i in self._tasks)+self.list_message[1])
