import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate('tank-battle/game/connect_fb_db/firebase_config.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pythonfbtesting-default-rtdb.firebaseio.com/'
})


def set_color_selected(player, color_selected):
    """
    will tell oppenent if you selected a color
    """
    ref = db.reference('Players')
    pla_ref = ref.child(player)

    pla_ref.update({

        'color_selected': color_selected
    })

def get_color_selected(player):
    """
    function will return if opponent selceted a color
    """
    ref = db.reference('Players')
    pla_ref = ref.child(player)
    selected_opponent = pla_ref.child('color_selected').get()
    return selected_opponent



def set_color(player, color):
    """
    will tell opponent your color
    """
    ref = db.reference('Players')
    pla_ref = ref.child(player)

    pla_ref.update({

        'color': color
    })

def get_color(player):
    """
    function will return opponents tank color
    """
    ref = db.reference('Players')
    pla_ref = ref.child(player)
    color_opponent = pla_ref.child('color').get()
    return color_opponent

def set_directions(player, dx, dy, fire, player2):
    """
    tells opponent how your tank is moving
    """
    ref = db.reference('Players')
    pla_ref = ref.child(player)
    pla2_ref = ref.child(player2)

    pla_ref.update({
        'dx': dx,
        'dy': dy,
        'fire': fire
    })
    direction_opponent = {}
    direction_opponent = pla2_ref.get()
    return direction_opponent['dx'], direction_opponent['dy'], direction_opponent['fire']

def set_pointer(player, dx, dy, select):
    """
    tells opponent how your tank is moving
    """
    ref = db.reference('Players')
    pla_ref = ref.child(player)

    pla_ref.update({
        'dx': dx,
        'dy': dy,
        'color_selected': select
    })

def get_pointer(player):
    """
    function will return opponents tank possion entered keys
    dx    dy    select
    """
    ref = db.reference('Players')
    pla_ref = ref.child(player)
    direction_opponent = {}
    direction_opponent = pla_ref.get()
    return direction_opponent['dx'], direction_opponent['dy'], direction_opponent['color_selected']