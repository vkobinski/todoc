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
    for todo in printList:
        current_index += 1
        print("({0}) {1}: {2}".format(current_index,todo.prefix, todo.body))
    return printList

def printTodoCount(printList):
    print("You have {0} TODOS:".format(len(printList)))


def usage():
    print("Usage: todoc <SUBCOMMAND>")
    print("SUBCOMMANDS:")
    print("    list        List All Your TODOs")
    print("    add         Add a TODO")
    print("    remove      Mark a TODO as Completed")

def listFromFile(caminho):
    todos = []
    mode = 'r' if os.path.exists(caminho) else 'a+'
    with open(caminho, mode) as file:
        for line in file:
            todos.append(line.replace("\n"," "))
    return todos

if len(sys.argv) < 2:
    print("Not enough arguments")
    usage()
    exit(1)
else:
    caminho = os.path.expanduser("~/todo.txt")
    if tokens[0] == 'list':
        todos = listFromFile(caminho)
        printTodoCount(todos)
        todoByImportance(todos)
    if tokens[0] == 'add':
        prefix = int(input("Insert the TODO importance (1-9): "))
        body = input("Insert the TODO description: ")
        final_body = "{0}: {1} \n".format("TOD"+ ("O"*prefix), body)
        with open(caminho, 'a+') as file:
            file.write(final_body)
    if tokens[0] == 'remove':
        # TODOO(#1): Implement the Remove Arg
        todos = listFromFile(caminho)
        printTodoCount(todos)
        todos = todoByImportance(todos)
        remove = int(input("Insert the TODO index you want to remove: "))
        todos.pop(remove-1)
        with open(caminho, 'w') as file:
            for todo in todos:
                todo_prefix = todo.prefix + ("O" * todo.importance)
                final_body = "{0}: {1} \n".format(todo_prefix, todo.body)
                file.write(final_body)
