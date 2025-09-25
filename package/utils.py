from datetime import datetime as dt

import json
import os

HR_STR = "\n" + "="*40 + "\n"

# ===== VALIDATION DATE ===== #
def is_valid_date(val_date):
    try:
        valid = dt.strptime(val_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# ===== GET DATA JSON ===== #
def load_json(file_name):
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error: {e}")
    else:
        return []

# ===== SAVE DATA JSON ===== #
def save_json(file_name, content):
    try:
        with open(file_name, "w") as f:
            json.dump(content, f, indent=2)
    except Exception as e:
        print(f"Error: {e}")

