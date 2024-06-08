class task:
	def __init__(self,description):
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
		self._tasks = []
		self.list_message = ["Task list:\n"
				"================================================================================\n"
				"   ID Description                                      State     Pri. Date      \n",
				"\n--------------------------------------------------------------------------------\n"
				"================================================================================\n"]
	
	def msg_pending(self):
		pending_list = []
		for i in self._tasks:
			if i._state == "pending":
				pending_list.append(i)
		print(self.list_message[0])
		for i in pending_list:
			print("   ",i._id, i._description+(49-len(i._description))*" "+i._state,"  ",i.priority)
		print(self.list_message[1])
			
	
	def msg(self):
		return str(self.list_message[0]+'\n'.join(i for i in self._tasks)+self.list_message[1])
		
		

		
