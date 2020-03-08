# IMPORTS
import requests
import json
import time

# SCRIPTS


# UTILS
from .header import header

def item_interaction(item, type ='take'):
    slug = type + '/'
    print(slug)
    JSON_DUMPS_obj = {"name": item}
    # - - - - 

    # Request
    result = requests.post(f'https://lambda-treasure-hunt.herokuapp.com/api/adv/{slug}',
        data=json.dumps(JSON_DUMPS_obj),
        headers=header,
    ).json()

    # Respect Cooldown -- from NEW ROOM object
    print(result['cooldown'])
    time.sleep(result['cooldown'])
    # - - - - 

    return result



    # Get current status
    playerStatus = getStatus()
    # - - - - 

    # Examine item or player
    print(f'JSON DUMPS : {JSON_DUMPS_obj}')
    result = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', 
        data=json.dumps(JSON_DUMPS_obj),
        headers=header,
    ).json()
    print(result)

    # Respect Cooldown -- from NEW ROOM object
    print(result['cooldown'])
    time.sleep(result['cooldown'])
    # - - - - 

    # Pick up treasure
    print(playerStatus['encumbrance'])
    print(result['weight'])
    print(playerStatus['strength'])

    # if result['name'] == 'tiny treasure' or result['name'] == 'small treasure' and playerStatus['encumbrance'] + result['weight'] < playerStatus['strength']:
    if playerStatus['encumbrance'] + result['weight'] < playerStatus['strength']:

        print(f'PICK IT UP')
        
        interaction_RESULT = item_interaction(result['name'])
        print(interaction_RESULT)
    # - - - - 

    return result