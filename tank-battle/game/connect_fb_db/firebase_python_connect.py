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

def set_directions(player, dx, dy):
    """
    tells opponent how your tank is moving
    """
    ref = db.reference('Players')
    pla_ref = ref.child(player)

    pla_ref.update({
        'dx': dx,
        'dy': dy
    })

def get_directions(player):
    """
    function will return opponents tank possion entered keys
    dx    dy
    """
    ref = db.reference('Players')
    pla_ref = ref.child(player)
    direction_opponent = {}
    direction_opponent = pla_ref.get()


    return direction_opponent['dx'], direction_opponent['dy']

def set_fire(player, fire):
    """
    tells opponent if you fired
    """
    ref = db.reference('Players')
    pla_ref = ref.child(player)

    pla_ref.update({

        'fire': fire
    })

def get_fire(player):
    """
    function will return if opponent has fired
    """
    ref = db.reference('Players')
    pla_ref = ref.child(player)
    fire_opponent = pla_ref.child('fire').get()
    return fire_opponent


# options = 0
# while options == 0:
#     color = get_color("player1")
#     print(color)
#     options = int(input("enter number: "))

# def change_color(color):
#     ref = db.reference('Players')
#     pla_ref = ref.child('player1')

#     pla_ref.update({

#         'color': color
#     })


# ref = db.reference('Employee')
# ref.update({

#     'emp1/lname': 'updated lname1',
#     'emp2/lname': 'updated lname2'
# })

# lame = db.reference('Employee2')

# emp_ref = lame.push({
#     'emp12': {
#         'password': 12345,
#         'name': 'Parwiz',
#         'lname': 'Forogh',
#         'age': 24
#     }
# })

# ref = db.reference('Employee2')
# emp_ref = ref.child('emp1')

# emp_ref.update({

# })


"""get info format"""
# ref = db.reference('Employee')
# emp_ref = ref.child('emp1')
# name = emp_ref.child('name').get()

# print(name)