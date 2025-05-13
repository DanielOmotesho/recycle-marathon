import pgzrun
import random
WIDTH=800
HEIGHT=600

CENTRE=(WIDTH/2,HEIGHT/2)

FINAL_LEVEL=7
START_SPEED=10
ITEMS=["plastic","battery","bottle","chips"]
game_over=False
game_complete=False
current_level=1
items=[]
animations=[]

def draw():
    global items
    screen.clear()
    screen.blit("a",(0,0))
    if game_over:
        display_message("YOU LOST","TRY AGAIN")
    elif game_complete:
        display_message("YOU WIN","WELL DONE")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items)==0:
        items=make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create=get_option_to_create(number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create=["paper"]
    for i in range(0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for i in items_to_create:
        item = Actor(i+"img")
        new_items.append(item)

    return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout)+1
    gap_size=WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        x_pos=(index+1)*gap_size
        item.x=x_pos
        


pgzrun.go()

          
    
