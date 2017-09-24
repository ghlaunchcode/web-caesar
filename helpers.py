#globals, yeesh!
strAlphaLC = "abcdefghijklmnopqrstuvwxyz"
strAlphaUC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_position(letter):
    return strAlphaLC.find(letter.lower())

def rotate_character(char, rot):
    #note: as a C programmer, I detest using char as varname ;)
    if( char.isalpha() ):
        if( strAlphaLC.find(char) > -1 ):
            return strAlphaLC[( alphabet_position(char) + rot ) % 26 ]
        else:
            return strAlphaUC[( alphabet_position(char) + rot ) % 26 ]
    else:
        return char