import requests
import json

# env....
import environ



env = environ.Env(
    DEBUG=(True)
)

def getStatus():
    print(f'---inside getStatus---')
    # TOKEN = env('TOKEN')
    # print(TOKEN)
    # return TOKEN

    all_rooms = requests.get(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/status/').json()