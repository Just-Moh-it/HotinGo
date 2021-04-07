
# Globally accessed variables across main.py
sec_ques=("What was the first movie you watched at the cinema?",
    "Where were you born?",
    "What was the name of your first pet?",
    "What is your favourite dish?",
    "What brand was your first car of?",
    "what is your favourite movie?",
    "What is your favourite colour?")

acceptables=(*[chr(i) for i in range(97,123)], "_",*[str(i) for i in range(10)], ".")


#============Python Functions==========

def acceptable(*args, acceptables=(*[chr(i) for i in range(97,123)], "_",*[str(i) for i in range(10)], ".")):
    '''
        If the characters in StringVars passed as arguments are in acceptables return True, else returns False
    '''
    for arg in args:
        for char in arg:
            if char.lower() not in acceptables:
                return False
    return True

# 
def printer(*args):
    '''
        Takes arguments like that in print and returns string like print() function
    '''
    returner=''
    for posa, arg in enumerate(args):
        if type(arg) in (list, tuple):
            for posi, item in enumerate(arg):
                returner+=(", " if posi!=0 else "\n\t")+item+("\n" if posi==len(arg)-1 else "")
        else:
            returner+=(" " if not returner[-1:]=="\n" and posa!=0 else "")+arg
    return returner

def return_rooms():
    pass