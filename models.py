#============Python Functions==========

# If the characters in StringVars passed as arguments are in acceptables return True, else returns False
def acceptable(*args, acceptables=(*[chr(i) for i in range(97,123)], "_",*[str(i) for i in range(10)], ".")):
    for arg in args:
        for char in arg:
            if char.lower() not in acceptables:
                return False
    return True

# Takes arguments like that in print and returns string like print() function
def printer(*args):
    returner=''
    for posa, arg in enumerate(args):
        if type(arg) in (list, tuple):
            for posi, item in enumerate(arg):
                returner+=(", " if posi!=0 else "\n\t")+item+("\n" if posi==len(arg)-1 else "")
        else:
            returner+=(" " if not returner[-1:]=="\n" and posa!=0 else "")+arg
    return returner

