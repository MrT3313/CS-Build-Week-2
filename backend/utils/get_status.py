import requests
import json
import time

def getStatus():
    '''
    This is a singled out 'make_request()' just because it will be used so much
    '''
    activeStatus = requests.get(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/status/'
    ).json()

    # COOLDOWN
    cooldown = activeStatus['cooldown']
    if activeStatus:
        print(f'-*- COOLDOWN/\n{cooldown}')
    time.sleep(activeStatus['cooldown'])
    # - - - - 

    return activeStatus

