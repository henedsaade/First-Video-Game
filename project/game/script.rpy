# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define hened = Character("Hened")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Detective Fauteux

    # These display lines of dialogue.

    Detective Fauteux "Hello Detective! I am Detective Fauteux. I've invited you here because there's been a series of murders plaguing our town."

    Detective Fauteux "We need your expertise to help us solve these cases. Are you willing to help us?"

    # This ends the game.

    return
