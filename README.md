# Trabalho1_POO
 O objetivo do seu trabalho é produzir um programa Python que permite gerenciar tarefas a fazer através da linha de comando Unix. O programa permitirá criar, listar e alterar estado de tarefas.

O programa deve dispor de três comandos, cada um com diversas opções.

- O comando list lista tarefas registradas.
- O comando new registra (cria) uma nova tarefa.
- O comando task permite realizar operações sobre uma tarefa já registrada.

As tarefas têm as seguintes características:

1) Um identificado, que é um inteiro positivo único para cada tarefa.
2) Uma descrição, que é uma cadeia de caracteres que diz o que deve ser feito.
3) Um estado, que pode ser "pending" se a tarefa ainda precisa ser executada, "done" se ela já foi concluída ou "cancelled" se ela foi cancelada.
4) Uma prioridade, que pode ser um dos valores 1, 2 ou 3.
5) Opcionalmente, a tarefa pode também ter uma data, que é a data final para conclusão.

## Executando o programa
Quando executado sem parâmetros, o programa apenas escreve uma mensagem de apresentação.

  ./todo.py 
Command line task manager.
Run with -h for help.

Quando executado com "-h" ele apresenta uma mensagem de ajuda breve, listando os comandos disponíveis:

 ./todo.py -h
usage: todo.py [-h] {list,task,new} ...

Manage your tasks in the command line.

options:
  -h, --help       show this help message and exit

commands:
  Main commands

  {list,task,new}
(Como em todos os exemplos, as mensagens não precisam ser exatamente as mostradas.)

### O comando list
O comando list, quando apresentado sozinho, apresenta uma lista abreviada, em forma de tabela, das tarefas pendentes. Cada tarefa deve ocupar exatamente uma linha, e cada linha deve ser limitada a no máximo 80 caracteres. Todas as informações da tarefa devem ser apresentadas. Se a descrição for muito grande de modo que as informações não caberiam nas 80 colunas da linha, você deve truncar a cadeia da descrição. Se a tarefa tem uma data, a data deve ser apresentada no formato ISO: AAAA-MM-DD, por exemplo 2024-05-20.

Se for fornecida a opção "-a" ou "--all" ao comando list, então todas as tarefas devem ser incluídas, e não apenas as pendentes.

Se for fornecida a opção "-p <x>", ou "--priority <x>", onde "<x>" é um número 1, 2 ou 3, devem ser incluídas apenas as tarefas pendentes que tem prioridade "<x>".

Se forem fornecidas as opções "-a" e "-p" simultaneamente, então todas as tarefas com a prioridade pedida devem ser incluídas, e não apenas as pendentes.

Se for fornecida a opção "-h" ou "--help" ao comando list, ele deve fornecer um texto com informações sobre o uso:

 ./todo.py list -h
usage: todo.py list [-h] [-a] [-p {1,2,3}]

List the tasks

options:
  -h, --help            show this help message and exit
  -a, --all             List all tasks, not only pendent
  -p {1,2,3}, --priority {1,2,3}
                        Show tasks with a given prioriy
### O comando new
O comando new deve sempre ser seguido da cadeia de caracteres com a descrição da tarefa. Por causa do jeito como o Unix lida com a linha de comando, essa cadeia de descrição deve ser fornecida entre aspas. A tarefa é criada com um número de identificação novo, que ainda não foi usado para outra tarefa, no estado "pending", com prioridade 2 e sem data associada.

Se for fornecida a opção "-h" ou "--help", o comando dá informações breves sobre a forma de uso:

 ./todo.py new -h
usage: todo.py new [-h] description

Create a task

positional arguments:
  description  Create a new task

options:
  -h, --help   show this help message and exit
  
### O comando task
Este comando permite fazer operações sobre uma tarefa existente. Ele deve ser seguido do número de identificação da tarefa (que pode ser lido na saída do comando list).

Se o comando é fornecido sem opções, ele escreve na tela as informações sobre a tarefa, em formato mais livre do que o usado no comando list, incluindo o texto completo da descrição.
Se ele recebe a opção "-d" ou "--done", então a tarefa indicada é marcada no estado "done".
Se ele recebe a opção "-c" ou "--cancelled", então a tarefa é marcada no estado "cancelled".
Se ele recebe a opção "-r" ou "--remove", a tarefa iindicada é removida da lista de tarefas. O número de identificação dessa tarefa não pode ser reutilizado para novas tarefas.
Se ele recebe a opção "-p <x>" ou "--priority <x>", então a prioridade  da tarefa é mudada para "<x>" e ele for 1, 2 ou 3. Se o valor de "<x>" for outro, um erro é indicado e nada é feito.
Se ele recebe a opção "-s <data>" ou "--schedule <data>", então se marca a data especificada por "<data>" para essa tarefa. Note que "<data>" deve estar no formato ISO: 2024-05-20.
Se ele recebe a opção "-h" ou "--help", então uma breve descrição de uso é apresentada:
 ./todo.py task -h
usage: todo.py task [-h] [-d | -c | -r | -s SCHEDULE | -p {1,2,3}] id

Act on a task

positional arguments:
  id                    Specify task id

options:
  -h, --help            show this help message and exit
  -d, --done            Mark task as done
  -c, --cancelled       Mark task as cancelled
  -r, --remove          Remove task
  -s SCHEDULE, --schedule SCHEDULE
                        Schedule the task
  -p {1,2,3}, --priority {1,2,3}
                        Change priorty level
## Pontos importantes
- O seu código deve usar orientação a objetos. Pelo menos as tarefas devem ser representadas internamente através de uma classe, usando apropriadamente encapsulação.
- Sempre que o usuário pedir para fazer algo que não faz sentido, o programa deve dar uma mensagem dizendo qual é o problema e não fazer nada. Por exemplo, ao tentar agir sobre uma tarefa inexistente, ou usar uma prioridade inexistentes, ou usar uma data inválida.
- Para a representação interna de datas, use o módulo datetime. Ele já permite conversão de cadeias no formato ISO para uma data e de uma data para cadeias ISO. Ele também faz a verificação se a data fornecida é válida.
- Para lidar com os parâmetros de linha de comando, use o módulo argparse. Como uma dica, crie um subparser para cada um dos comandos list, new e task, para permitir que as diferentes opções sejam tratadas adequadamente para cada comando.
- Use docstrings para documentar seu código.
- Como cada execução é independente (e programa não fica rodando esperando comandos do usuário), as informações sobre tarefas devem sempre ser guardadas em um arquivo. Seu programa deve então começar lendo esse arquivo, fazendo a operação pedida, e re-escrevendo o arquivo antes de sair. O arquivo precisa conter tanto as informações das tarefas quando o número do próximo identificador de tarefas livre. Vocês podem escolher o formato desse arquivo, mas eu sugiro um simples arquivo de texto, com campos separados por um caractere escolhido.
