from datetime import datetime as dt
from utils import load_json, save_json, is_valid_date
import uuid

def add_todo(title, content, due_date):
    rand_id = str(uuid.uuid4())
    sort_id = rand_id[0:8]
    create_date = dt.now().strftime("%Y-%m-%d")

    json_struc = {
        "id": rand_id,
        "sort_ud": sort_id,
        "title": title,
        "content": content,
        "created": create_date,
        "due_date": due_date,
        "is_done": False
    }

    return json_struc

def create_todo(file_name):
    data = load_json(file_name)

    input_title = input("Title >>> ").title() or "Untitled"
    input_content = input("Description >>> ") or "Not described"

    while True:
        input_due_date = input("Due Date (format: YYYY-MM-DD) >>> ")
        if is_valid_date(input_due_date):
            break
        else:
            print("Invalid Format, Correct Format (YYYY-MM-DD)")

    new_todo = add_todo(input_title, input_content, input_due_date)
    data.append(new_todo)
    save_json(data)
