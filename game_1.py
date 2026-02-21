import random

def game_play(choice, result):
    print("""
    =============================
    ******* START  GAME 1 *******
    **** Rock Paper Scissors ****
    =============================
    """)
    bot_choice = random.choice("rps")
    print(f"Select player: {str.capitalize(choice)}")
    print(f"Select bot: {str.capitalize(bot_choice)}")

    if str.lower(choice) == bot_choice:
        print("Result of game - DRAW")
        print(f"Score,"
              f"\n\tplayer: {result['player']}"
              f"\n\tbot: {result['bot']}")
    elif str.lower(choice) == "r" and bot_choice == "p":
        result['bot'] += 1
        print("Result of game - BOT WINS")
        print(f"Score,"
              f"\n\tplayer: {result['player']}"
              f"\n\tbot: {result['bot']}")
    elif str.lower(choice) == "r" and bot_choice == "s":
        result['player'] += 1
        print("Result of game - PLAYER WINS")
        print(f"Score,"
              f"\n\tplayer: {result['player']}"
              f"\n\tbot: {result['bot']}")
    elif str.lower(choice) == "p" and bot_choice == "s":
        result['bot'] += 1
        print("Result of game - BOT WINS")
        print(f"Score,"
              f"\n\tplayer: {result['player']}"
              f"\n\tbot: {result['bot']}")




result = {"bot": 0,
          "player": 0
          }
choise = input("Select your choice /P - R - S/:\n\t>>> ")
game_play(choice=choise, result=result)
















