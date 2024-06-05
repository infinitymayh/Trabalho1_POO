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

class list:
	def __init__(self):
		self._tasks = {}
	
	def add(self, task):
		self._tasks[len(self.tasks)+1] = task
