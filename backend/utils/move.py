# IMPORTS
import requests
import time
import pdb

# SCRIPTS
from .make_request import make_request

# UTILS
from .header import header

# PRINT
LIVE_print = True 
DEBUG_print = True

def move(direction, current_room):
        print(f'- 🏃‍♂️ - Attempting MOVEMENT/\n {direction} from {current_room}')

        # TODO: this..
        # wise explorer
        wise_result = False

        # Set request data
        if wise_result is False:
            JSON_DUMPS_obj = {
                "direction": direction,
            }
        else:
            JSON_DUMPS_obj = {
                "direction": direction,
                "next_room_id": wise_result
            }
        # Debug
        if DEBUG_print:
            print(f'---DEBUG--- JSON_DUMPS_obj/\n{JSON_DUMPS_obj}')
        # - - - - 

        # Move Player
        newRoom_OBJECT = make_request(
            'POST',
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/', 'move', 
            header,
            JSON_DUMPS_obj
        )

        # Return
        return newRoom_OBJECT