import json, requests
todos = []

def get_todos():
    global todos
    return todos

def add_one_task(title):
    global todos
    todos.append({ "label": title, "done": False })

def print_list():
    global todos
    print("Your current list of tasks ("+str(len(todos))+"):")
    count = 1
    for t in todos:
        status = "✓ done" if t["done"] else "𝙭 pending"
        print(" "+str(count)+". "+t["label"]+" - "+status)
        count = count + 1

def delete_task(number_to_delete):
    global todos
    new_todos = []
    number_to_delete = int(number_to_delete) - 1
    for i in range(0,len(todos)):
        if str(i) != str(number_to_delete):
            new_todos.append(todos[i])

    todos = new_todos

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

    
def save_todos():
    global todos
    headers = {'Content-type': 'application/json'}
    payload = json.dumps(todos)
    r = requests.put(url = 'https://assets.breatheco.de/apis/fake/todos/user/alesanchezr', data = payload, headers=headers) 
    response_data = r.json()
    print(response_data['result'])


def load_todos():
    global todos
    r = requests.get(url = 'https://assets.breatheco.de/apis/fake/todos/user/alesanchezr') 
    if(r.status_code == 200):
        todos = r.json()
    else:
        print(r.json())

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
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")