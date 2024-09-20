import requests
import random
def random_pokemon():
    id_list = range(1, 52)
    id = random.choice(id_list)
    return id

def api_call(id):
    url = f'https://pokeapi.co/api/v2/pokemon/{id}/'
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'].capitalize(),
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'experience': pokemon['base_experience']
    }

def battle(player_pokemon, bot_pokemon):
    win = input(f'Which characteristic of {player_pokemon['name']} '
                f'will win against {bot_pokemon['name']}? (id/height/weight/experience) ')
    win_choice = win.lower()

    bot_charac = bot_pokemon[win_choice]
    player_charac = player_pokemon[win_choice]

    bot_charac = bot_pokemon[win_choice]
    player_charac = player_pokemon[win_choice]


    if win_choice == 'id':
       print(f'{player_pokemon['name']} {win_choice} is {player_charac}')
       print(f'{bot_pokemon['name']} {win_choice} is {bot_charac}'),
    elif win_choice == 'height':
       print(f'{player_pokemon['name']} {win_choice} is {player_charac / 10}m.')
       print(f'{bot_pokemon['name']} {win_choice} is {bot_charac / 10}m.'),
    elif win_choice == 'weight':
       print(f'{player_pokemon['name']} {win_choice}s {player_charac / 10}kg.')
       print(f'{bot_pokemon['name']} {win_choice}s {bot_charac / 10}kg.'),
    elif win_choice == 'experience':
       print(f'{player_pokemon['name']} base {win_choice} is {player_charac}.')
       print(f'{bot_pokemon['name']} base {win_choice} is {bot_charac}.'),


    if player_charac > bot_charac:
       print('Player Wins!'),
    elif bot_charac > player_charac:
       print('Bot Wins!')
    else:
       print("It's a draft!")


def play():
    player_pokemon_id = random_pokemon()
    player_pokemon = api_call(player_pokemon_id)

    bot_pokemon_id = random_pokemon()
    bot_pokemon = api_call(bot_pokemon_id)

    print(f'Your pokemon is {player_pokemon['name']}'),
    print(f'Bot pokemon is {bot_pokemon['name']}'),
    battle(player_pokemon, bot_pokemon)


play()







