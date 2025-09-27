import random

scores = {
    "User": 0,
    "Bot": 0
}

win_rule = {
    "batu": "gunting",
    "gunting": "kertas",
    "kertas": "batu"
}

choice = list(win_rule.keys())

def get_winner(user, bot):
    if user == bot:
        return "Draw"
    elif win_rule[user] == bot:
        return "User"
    else:
        return "Bot"

def start_game():
    bot = random.choice(choice)
    user = input("Pilih (batu/gunting/kertas): ").lower()

    if user not in choice:
        print("Hanya boleh pilih: batu, gunting, atau kertas!")
        return

    print(f'User: {user} VS Bot: {bot}')
    winner = get_winner(user, bot)

    if winner == "Draw":
        print("Draw")
    else:
        print(f"{winner} Win")
        scores[winner] += 1

def main():
    try:
        while True:
            start_game()
            print(f'''
======================
User: {scores["User"]}
Bot : {scores["Bot"]}
======================
''')
    except KeyboardInterrupt:
        print("\nForce Close")

if __name__ == "__main__":
    main()
