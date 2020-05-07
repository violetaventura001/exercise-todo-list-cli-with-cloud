import json, requests

todos = []

def get_todos():
    return todos

def add_one_task(title):
    todos.append(title)

def print_list():
    todos
    print("These are your to-do task: \n "+str(todos))

def delete_task(number_to_delete):
    if number_to_delete in todos:
        todos.remove(number_to_delete)
    else:
        print(number_to_delete +" "+ "does not exsist in this list.")
    return todos  

def initialize_todos():
    global todos
    r = requests.get('https://assets.breatheco.de/apis/fake/todos/user/alesanchezr') 
    if(r.status_code == 404):
        print("No previous todos found, starting a new todolist")
        r = requests.post(url = 'https://assets.breatheco.de/apis/fake/todos/user/alesanchezr', data = []) 
        if r.status_code == 200:
            print("Tasks initialized successfully")
    else:
        print("A todo list was found, loading the todos...")
        todos = r.json()
    
def save_todos(listToUpdate):
    with open("todos.csv","w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(listToUpdate)
        csvfile.close() 
    return listToUpdate

def load_todos():
    with open('todos.csv') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        for row in csvreader:
            print(', '.join(row
            ))
        csvfile.close()
    
# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    stop = False
    print("Initializing todos with previous data or creating a new todo's list...")
    initialize_todos()
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Send/Save todo's to API
        5. Retrieve todo's from API
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos(todos)
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")