import sys
import os
from utils import *

tokens = sys.argv[1:]

def todoByImportance(todos):
    printList = []
    current_index = 0
    for todo in todos:
        current = Todo(todo)
        printList.append(current)
    printList.sort(key=lambda x: x.importance, reverse=True)
    print("You have {0} TODOS:".format(len(printList)))
    for todo in printList:
        current_index += 1
        print("{0}° {1}: {2}".format(current_index,todo.prefix, todo.body))

def usage():
    print("Usage: todoc <SUBCOMMAND>")
    print("SUBCOMMANDS:")
    print("    list        List All Your TODOs")
    print("    add         Add a TODO")
    print("    complete    Mark a TODO as Completed")

if len(sys.argv) < 2:
    print("Not enough arguments")
    usage()
    exit(1)
else:
    caminho = os.path.expanduser("~/todo.txt")
    if tokens[0] == 'list':
        todos = []
        mode = 'r' if os.path.exists(caminho) else 'a+'
        with open(caminho, mode) as file:
            for line in file:
                todos.append(line.replace("\n"," "))
        todoByImportance(todos)
    if tokens[0] == 'add':
        prefix = int(input("Insert the TODO importance (1-9): "))
        body = input("Insert the TODO description: ")
        final_body = "{0}: {1} \n".format("TOD"+ ("O"*prefix), body)
        with open(caminho, 'a+') as file:
            file.write(final_body)
    if tokens[0] == 'complete':
        assert False, "Not yet implemented"
