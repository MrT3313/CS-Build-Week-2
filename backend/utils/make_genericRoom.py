# IMPORTS


def make_genericRoom(current_room):
    vertex_data = {
        'room_id': current_room['room_id'],
        'exits': {
            "n" : '?',
            "s" : '?',
            "e" : '?',
            "w" : '?',
        }
    }
    walls = [exit for exit in ['n','s','e','w',] if exit not in current_room['exits'] ]
    for dir in vertex_data['exits']:
        if dir in walls:
            print(vertex_data['exits'][dir])
            vertex_data['exits'][dir] = None
    # for exit in walls:
    #     vertex_data[exit] = None

    return vertex_data