# IMPORTS
import json

# UTILS
import .header import header

# __ MAIN __
def examine():
    examine_result = requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', 
        '''
        This is a singled out 'make_request()' just because it will be used so much
        '''
        data=json.dumps(JSON_DUMPS_obj),
        headers=header,
    ).json()

    return examine_result