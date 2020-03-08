# TIME
import time

# SCRIPTS
from utils.make_request import make_request

# UTILS
from utils.header import header


# __ MAIN FUNCTION __ 
def initialization():
    startingRoom = make_request(
        'GET', 
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/', 'init', 
        header 
        #  no data
    )
    # - - - - 
    print(f'STARTING ROOM: {startingRoom}')
    
    # COOLDOWN
    print(startingRoom['cooldown'])
    time.sleep(startingRoom['cooldown'])

    # Return
    return startingRoom