from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below:")
print("It is", now)


while True:
    user_action = input("Select action(add,new show, complete or edit (or exit)): ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)
    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, x in enumerate(todos):
            x = x.strip("\n")
            print(f"{index+1}. {x}")
    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()

            print("here is existing todos:")
            for index, x in enumerate(todos):
                x = x.strip("\n")
                print(f"{index+1}. {x}")

            number = int(user_action[5:])
            number = number - 1
            new_todo = input("input edited todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid, try putting the number")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()

            tdel = int(user_action[9:])
            todo_to_remove = todos[tdel-1]
            todos.pop(tdel-1)

            todo_to_remove = todo_to_remove.strip("\n")

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
print("bye!")
