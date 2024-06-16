Trabalho 1 - Gerenciador de tarefas - Programação Orientada a Objetos (IFSC-USP)

Grupo: Kevyn Reis e Mayara Soares


O objetivo do trabalho é produzir um programa Python que permite gerenciar tarefas a fazer através da linha de comando Unix. O programa permitirá criar, listar e alterar estado de tarefas.

Na linha de comando, o comando deve ser escrito como "python3 main.py" e seguido dos comandos separados por espaço.

Os comandos principais disponíveis são: "list", "task" e "new", tendo cada um subcomandos e o comando "-h" ou "--help" para ajuda.

!!! Os comandos deveriam ser gerenciados pelo argparse, mas como não foi possível fazê-lo a tempo, foi decidido usar strings para as mensagens de ajuda e estrutura condicional para a análise da entrada do usuário. Neste caso, o comando "task" deve sempre ser seguido de "-h"/"--help" ou do id da tarefa e só então os comandos que agem sobre a tarefa ("-p"/"--priority", "-r"/"--remove", "-c"/"--cancelled", "-d"/"--done", "-s"/"--schedule").

O script "Objects.py" guarda funções extensas ou que abrem/criam/mudam o arquivo "task_list.pkl" e a classe task que cria os objetos do tipo tarefa. É nele que são acessadas as listas e salvadas as tarefas.