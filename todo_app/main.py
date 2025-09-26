import os
SEPARATOR = "\n" + "="*40 + "\n"

# ===== DATA TASK ===== #
TASKS = []

# ===== MENUS ===== #
MENU_MAIN = SEPARATOR
MENU_MAIN += '''
[1]. Tambah
[2]. Hapus
[3]. Lihat
[4]. Edit
[5]. Keluar
'''
MENU_MAIN += SEPARATOR
TASK_NOT_FOUND = "Tugas Tidak Ditemukan!"

# ===== CLEAR TERMINAL FUNCTION ===== #
def clear_terminal():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

# ===== ADD TASK FUNCTION ===== #
def add_task():
    while True:
        new_task = input("Masukkan Tugas: ")
        if new_task:
            break
    
    TASKS.append(new_task)

# ===== SHOW TASK FUNCTION ===== #
def show_task():
    if TASKS:
        print(SEPARATOR)
        for i, v in enumerate(TASKS, start=1):
            print(f"[{i}]: {v}")
        print(SEPARATOR)
    else:
        print(TASK_NOT_FOUND)

# ===== DELETE TASK FUNCTION ===== #
def delete_task():
    if not TASKS:
        print(TASK_NOT_FOUND)
        return
    
    show_task()

    try:
        user_delete = int(input("Pilih Nomor Tugas Untuk Di Hapus: "))
    except ValueError:
        print("Hanya Boleh Angka")
        return
    
    try:
        TASKS.pop(user_delete - 1)
    except Exception:
        print(TASK_NOT_FOUND)

# ===== EDIT TASK FUNCTION ===== #
def edit_task():
    if not TASKS:
        print(TASK_NOT_FOUND)
        return

    try:
        show_task()
        user_edit = int(input("Pilih Nomor Tugas Untuk Di Edit: "))
        _ = TASKS[user_edit - 1]

        TASKS[user_edit - 1] = input("Isi Baru: ")

    except Exception as e:
        print(TASK_NOT_FOUND)

# ===== MAIN FUNCTION ===== #
def main():
    try:
        while True:
            clear_terminal()
            print(MENU_MAIN)

            try:
                user_opt = int(input("Pilih Opsi 1 - 4: "))
                if user_opt == 1:
                    add_task()
                elif user_opt == 2:
                    delete_task()
                elif user_opt == 3:
                    show_task()
                elif user_opt == 4:
                    edit_task()
                elif user_opt == 5:
                    print("Goodbye!...")
                    break
                else:
                    print("!Hanya angka 1 - 4")
            except ValueError:
                print("Only Numbers 1 - 3")
                

            input("\nPress Enter to continue...")
    except KeyboardInterrupt:
        print("\n!Force Close")

if __name__ == "__main__":
    main()
