from datetime import datetime as dt

import json
import os
import uuid

data = []

# ===== CREATE ADD TODO_LIST ===== #
def add_todo(title, content, due_date):
    idstr = str(uuid.uuid4())
    date = dt.now().isoformat()

    struc = {
                "id": idstr, 
                "title": title, 
                "content": content, 
                "create_date": date,
                "due_date": due_date,
                "is_done": False 
            }
    return struc

# ===== CREATE FUNCTION ===== #
def create():
    data_struc = []

    input_title = input("Title >>> ").title()
    input_content = input("Description >>> ")
    input_due_date = input("Due Date (YYYY-MM-DD) >>> ")

    new_todo = add_todo(input_title, input_content, input_due_date)

    if os.path.exists("data.json"):
        try:
            with open("data.json", "r") as f:
                data_struc = json.load(f)
        except Exception as e:
            print(f"Error {e}")

    data_struc.append(new_todo)
    try:
        with open("data.json", "w") as f:
            json.dump(data_struc, f, indent=4)

    except Exception as e:
        print(f"Error {e}")
        return

# ===== USER OPTION ===== #
def user_option():
    error_message = "Only Accept Numbers From 1 - 6"
    while True:
        menus = f'''
[1]. Create
[2]. Read
[3]. Update
[4]. Delete
[5]. Show List
[6]. Exit
==========
>>>> '''
        try:
            input_user = int(input(menus))
        
            if input_user == 1:
                print("1")
                create()
            elif input_user == 2:
                print("2")
            elif input_user == 3:
                print("3")
            elif input_user == 4:
                print("4")
            elif input_user == 5:
                print("5")
            elif input_user == 6:
                print("6")
                break
            else:
                print(error_message)
                continue

        except ValueError:
            print(error_message)
            continue

# ===== MAIN PROGRAM ===== #
def main():
    try:
        user_option()
    except KeyboardInterrupt:
        print("!Force Close")
        return

# ===== EXECUTION MAIN PROGRAM ===== #
if __name__ == "__main__":
    main()
