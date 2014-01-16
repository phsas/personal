# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
define s = Character('Sylvie McBerry', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")

label start:
    "I'll ask her..."

    m "Um... will you..."
    m "Will you be let me berry you?"

    "Silence."
    "She is shocked, and then..."

    s "Sure, but what does \"berry\" mean?"

    return
