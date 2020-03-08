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

First half of the day... total failure

Heres to round 2
^^ failure

-- SUNDAY --

12:05 - initial commit @ clean  
12:58 - alot of setup. finally getting my first question answered: Where am i??. Not using Django and now running into new package importing issues. Setting up a new python env rn...think thats the issues  
13:11 - env & function imports working. initializing player and getting current status  
13:55 - creating or reading .txt file with open()  
-- 7 min break ... -- 
14:54 - Error again... --> 
    ``` 
    attempted relative import beyond top-level package
    ```
16:04 - close to updating GOD_graph & INSTANCE_graph data
16:07 - updating ^^ under None case. file creation and updating working correctly



    