# IMPORTS 
import requests
import json
import time
import pdb

# __ MAIN __
def make_request(reqType, baseURL, slug='', header={}, data={}):
    '''
    Totally generic request maker
    Respects response cooldown before
    '''
    print(f'-- TRYING TO MAKE REQUEST --')
    debug = False
    print_cooldown = True

    # GET
    print(f'{reqType} -- {baseURL}{slug}/ -- {data}')
    if reqType == 'get' or reqType == 'Get' or reqType == 'GET':
        response_data = requests.get(baseURL + slug + '/',
            data=json.dumps(data),
            headers=header
        ).json()
    # - - - -
    
    # POST
    if reqType == 'post' or reqType == 'Post' or reqType == 'POST':
        response_data = requests.post(baseURL + slug,
            data=json.dumps(data),
            headers=header
        ).json()
    # - - - -
    
    cooldown = response_data['cooldown']

    # Debug
    if debug:
        print(response_data)
    # - - - - 

    # COOLDOWN
    if print_cooldown:
        print(f'-*- COOLDOWN/\n{cooldown}')
    time.sleep(response_data['cooldown'])
    # - - - -
    

    # Return
    return response_data