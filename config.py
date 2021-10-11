import tkinter as tk

# Configurations and Globals

config = {
    'DB_HOST': 'mohityadav.codes',
    'DB_PORT': 3306,
    'DB_NAME': 'hms',
    'DB_AUTOCOMMIT': True,

    # 'SEC_QUES':[
    # "What was the first movie you watched at the cinema?",
    # "Where were you born?",
    # "What was the name of your first pet?",
    # "What is your favourite dish?",
    # "What brand was your first car of?",
    # "what is your favourite movie?",
    # "What is your favourite colour?"
    # ],

    'acceptables': (*[chr(i) for i in range(97,123)], "_",*[str(i) for i in range(10)], "."),

    'windows': {
        'main_window': {
            'win_width': 840,
            'win_height': 450,
            'nav_width': 170
        }
    },

    'sidebar_button_positions': [
        
    ]
}

# Font
fonts = {
    'h1':('arial', 22, 'bold'),
    'h2':('arial', 18, 'bold'),
}