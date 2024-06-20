<<<<<<< HEAD
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            with open('todos.txt','r') as file:
                todos = file.readlines()
            
            todos.append(todo)

            with open('todos.txt','w') as file:
                file.writelines(todos)
            
        case "show":
            with open('todos.txt','r') as file:
                todos =  file.readlines()
            
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index+1} - {item}",sep="",end="")
                
        case "edit":
            number = int(input("Number of the todo to edit: ")) -1
            with open('todos.txt','r') as file:
                todos =  file.readlines()
            newtodo = input("Enter new todo: ")
            todos[number] = newtodo + "\n"
            with open('todos.txt','w') as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Number of the todo to complete: ")) -1
            with open('todos.txt','r') as file:
                todos = file.readlines()
            todos.pop(number)
            with open('todos.txt','w') as file:
                file.writelines(todos)
                removed = todos[number].strip('\n')
            print(f"Todo {removed} is now removed from the list.")
=======
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            with open('todos.txt','r') as file:
                todos = file.readlines()
            
            todos.append(todo)

            with open('todos.txt','w') as file:
                file.writelines(todos)
            
        case "show":
            with open('todos.txt','r') as file:
                todos =  file.readlines()
            
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index+1} - {item}",sep="",end="")
                
        case "edit":
            number = int(input("Number of the todo to edit: ")) -1
            with open('todos.txt','r') as file:
                todos =  file.readlines()
            newtodo = input("Enter new todo: ")
            todos[number] = newtodo + "\n"
            with open('todos.txt','w') as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Number of the todo to complete: ")) -1
            with open('todos.txt','r') as file:
                todos = file.readlines()
            todos.pop(number)
            with open('todos.txt','w') as file:
                file.writelines(todos)
                removed = todos[number].strip('\n')
            print(f"Todo {removed} is now removed from the list.")
>>>>>>> 6e4bf84439071a9e5da8dfa05fa0d27d65a1666a
