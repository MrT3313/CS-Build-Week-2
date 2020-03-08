We're here. 

We have recognized the high likleyhood of failure. 

What? 

We don't accept that. Action.

------

Why: 
1. Did not plan / split up the problem well
2. Did not forsee how a 'fresh start' on the traversal & and cooldowns & the lack of powerups on a 'fresh start' would delay making progress on an overall map understanding
3. I was not using my standing desk...
    ^ this is a joke. 
        ^ is it? 

-----

Prep Notes: 

1. BREAK THE LOOP...dont do everything in one loop. Have an action...make THAT action. 
    - move ... /move/right -- /move/left
    - (DFS) Find room WITHOUT unknown exit
        - based on DJANGO graph VS local GLOBAL_worldGraph
    - (BFS) Find room with unknown exit
        - based on DJANGO graph VS local GLOBAL_worldGraph
    - find specific room

-----

Steps:
1. DFS  
    ```md
    `current room`  
    find ?:  
        move forward  
    else:  
        YOUR DONE  
    ```
    1. What is my current room
        ```GET``` 
        - run getStatus()
        
        ```POST```
        - check `request.body.room` => if nothing run getStatus()
        - check `request.body.target` => if nothing use default '?' as the DFS target

        `ACTIVE_room`

    2. Initialize Variables
        - QUEUE_stack(ACTIVE_room)
        - QUEUE_path(ACTIVE_room['room_id'])

2. BFS
    - 

    

?? JSON serialization
``` 
class MyUniversalEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__json__"):
            return obj.__json__()
        return json.JSONEncoder.default(self, obj)

```
First half of the day... total failure

Heres to round 2
^^ failure

-- SUNDAY --

12:05 - initial commit @ clean


    