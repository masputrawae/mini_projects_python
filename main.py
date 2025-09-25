from datetime import datetime as dt

import json
import os
import uuid

FILE_NAME = "data.json"

# ===== VALIDATION DATE ===== #
def valid_date(input_date):
    try:
        date_obj = dt.strptime(input_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# ===== GET DATA JSON ===== #
def get_data(file_name):
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error: {e}")
    else:
        return []

# ===== SAVE DATA ===== #
def save_data(file_name, content):
    try:
        with open(file_name, "w") as f:
            json.dump(content, f, indent=4)
    except Exception as e:
        print(f"Error: {e}")

# ===== CREATE ADD TODO_LIST ===== #
def add_todo(title, content, due_date):
    idstr = str(uuid.uuid4())
    short_id = idstr[0:8]
    date = dt.now().isoformat()

    struc = {
                "id": idstr, 
                "short_id": short_id,
                "title": title, 
                "content": content, 
                "create_date": date,
                "due_date": due_date,
                "is_done": False 
            }
    return struc

# ===== CREATE FUNCTION ===== #
def create():
    data_struc = get_data(FILE_NAME)

    input_title = input("Title >>> ").title()
    input_content = input("Description >>> ")

    while True:
        input_due_date = input("Due Date (YYYY-MM-DD) >>> ")
        if valid_date(input_due_date):
            break
        else:
            print("Invalid Format, Correct Format (YYYY-MM-DD)")

    new_todo = add_todo(input_title, input_content, input_due_date)
    data_struc.append(new_todo)

    save_data(FILE_NAME, data_struc)

# ===== SHOW LIST ===== #
def show_list():
    data = get_data(FILE_NAME)
    hr = "\n" + "=" * 40 + "\n"
    sparator = hr
    sparator += "ALL TODO".center(40)
    sparator += hr
    print(sparator)
    if data:
        for i, v in enumerate(data, start=1):
            print(f'''
[{i}]. {v["title"]}
{"-"*40}
Short Id        :{v["short_id"]}
Description     :{v["content"]}
Created         :{v["create_date"]}
Due Date        :{v["due_date"]}
Is Done?        :{v["is_done"]}''')
            print(hr)
    else:
        print("No Tasks")

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
                create()
            elif input_user == 2:
                print("2")
            elif input_user == 3:
                print("3")
            elif input_user == 4:
                print("4")
            elif input_user == 5:
                show_list()
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
