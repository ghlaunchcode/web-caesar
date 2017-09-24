#import helpers
from helpers import alphabet_position, rotate_character

def rotate_string(text, rot):
    strRet = ""
    for c in text:
        strRet += rotate_character(c, rot)
    return strRet

#for testing:
def main():
    msg = input("Type a message:\n" )
    rot = int(input("Rotate by:\n" ))
    #msg = "Hello, World!"
    #rot = 5
    print( rotate_string(msg,rot))

if __name__ == "__main__":
    main()