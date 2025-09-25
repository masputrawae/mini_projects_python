import json

data = []

# ===== CREATE JSON FUNCTION ===== #
def create():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error: {e}")
        return

    if not data:
        print("data kosong")
    else:
        print(data)

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
