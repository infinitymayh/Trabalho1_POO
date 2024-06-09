class task:
	def __init__(self,n_id, description):
		self._id = n_id
		self._description = description
		self._state = "pending"
		self.priority = 2
	
	def priority(self, p=None):
		if p != None:
			self.priority = p
		return self.priority


list_message = ["Task list:\n"
				"================================================================================\n"
				"   ID Description                                      State     Pri. Date      \n",
				"\n--------------------------------------------------------------------------------\n"
				"================================================================================\n"]
	
def msg_pending():
	tarefa,estado=carregar_tarefas(nome_arquivo)
	print(list_message[0])
	for i in estado:
		if estado[i] == "pending":
			contagem = 0
			for j in tarefa[i]:
				contagem += 1
			print("   ",i,tarefa[i]," "*(47-contagem),estado[i],"  ",)
	print(list_message[1])
			
	
	def msg(self):
		return str(self.list_message[0]+'\n'.join(i for i in self._tasks)+self.list_message[1])
		
		
#=================================================================================================================

# salvar as tarefas

import json

#nome do arquivo das tarefas

nome_arquivo = 'tarefa.json'


# funcao para abrir o arquvivo das tarefas

def carregar_tarefas(nome_arquivo):
	try:
		with open(nome_arquivo,'r') as arquivo:
			dic = json.load(arquivo)
			if dic != 0:
				return dic["tarefas"],dic["estado"]
	except FileNotFoundError:
		return {},{}
        
#funcao para salvar as tarefas no arquivo

def salvar_tarefas(tarefas,estado, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump({"tarefas": tarefas, "estado": estado}, arquivo)
        

