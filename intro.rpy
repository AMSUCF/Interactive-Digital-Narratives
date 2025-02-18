# Setup and Introduction
# Player and opponent stats and selection variables
default player_hp = 40
default player_max_hp = 100
default opponent_hp = 60
default opponent_max_hp = 100
default player_creature = ""  # Will be set during selection
default friendship = 5

## Characters

define m = Character("Me", color="#c542b8")
define c = Character("[player_creature]", color="#0059ff")

## --- Screens ---

# Battle Interface (Pokémon-style layout)
screen battle_interface():
    modal True
    tag battle

    # Opponent's sprite (top-right)
    add "littlefoot.png" xalign .85 yalign .1

    # Player's creature sprite: choose image based on selection
    if player_creature == "Jackalope":
        add "jackalope.png" xalign .1 yalign .6
    elif player_creature == "Mothkid":
        add "mothkid.png" xalign .1 yalign .6
    elif player_creature == "Hypnotoad":
        add "hypnotoad.png" xalign .1 yalign .6

    # Opponent's HP bar (top-right)
    frame:
        xalign .95
        yalign 0.05
        background "#0009"
        padding (10, 5, 10, 5)  # left, top, right, bottom
        vbox:
            text "Wandering Creature" color "#FFF" size 18
            bar value opponent_hp range opponent_max_hp xalign 0.0 yalign 0.1 xmaximum 200

    # Player's HP bar (bottom-left)
    frame:
        xalign 0.05
        yalign .75
        background "#0009"
        padding (10, 5, 10, 5)
        vbox:
            text "[player_creature]'s HP" color "#FFF" size 18
            bar value player_hp range player_max_hp xalign 0.0 yalign 0.1 xmaximum 200

    # Battle options menu (centered)
    frame:
        xalign 0.5
        yalign 0.55
        background "#0009"
        padding (10, 10, 10, 10)
        hbox spacing 30:
            textbutton "Fight" action Return("fight") text_color "#FF0000"
            textbutton "Small Talk" action Return("talk") text_color "#00ff4c"
            textbutton "Compliment" action Return("compliment") text_color "#ad27bc"
            textbutton "Run" action Return("run") text_color "#4c00ff"

# Starter Selection Screen
screen creature_selection():
    modal True
    tag selection
    frame:
        xalign 0.5
        yalign 0.5
        background "#0009"
        padding (10, 10, 10, 10)
        vbox:
            spacing 30
            text "Choose your companion creature:" color "#fff" size 40
            textbutton "Jackalope" action [SetVariable("player_creature", "Jackalope"), Jump("battle_intro")] text_color "#FF0000" text_size 35
            textbutton "Mothkid" action [SetVariable("player_creature", "Mothkid"), Jump("battle_intro")] text_color "#FF0000" text_size 35
            textbutton "Hypnotoad" action [SetVariable("player_creature", "Hypnotoad"), Jump("battle_intro")] text_color "#FF0000" text_size 35

## --- Labels (Scenes) ---

label start:
    scene bg intro with fade
    "Welcome to the forest..."
    call screen creature_selection

label battle_intro:
    # Transition into the battle arena
    scene bg battle with dissolve
    "As you step into a clearing, a wandering creature blocks your path."
    "With your companion [player_creature] by your side, you're ready to face the challenge."
    jump battle_sequence

label battle_sequence:
    # Display the battle interface and wait for player's command.
    "The creatures face off..."
    show screen battle_interface
    $ result = ui.interact()  # Wait for selection from the battle menu

    if result == "fight":
        hide screen battle_interface
        "You launch an attack with [player_creature]!"
        "The wandering creature looks fightened and confused."
        $ opponent_hp -= 20
        if opponent_hp <= 0:
            "The wandering creature collapses, terrified."
            hide screen battle_interface
            jump victory
        else:
            "The wandering creature is still standing, but barely."
            jump battle_sequence

    elif result == "talk":
        hide screen battle_interface
        "The wandering creature is happy someone took an interest"
        $ player_hp += 20
        if player_hp == 100:
            "The creatures are now friends."
            hide screen battle_interface
            jump friendship
        else:
            "Both creatures are studying one another."
            jump battle_sequence

    elif result == "compliment":
        hide screen battle_interface
        "The wandering creature looks flattered and excited"
        $ player_hp += 20
        if player_hp == 100:
            "The creatures are both happy to connect."
            jump friendship
        else:
            "Both creatures are chattering happily."
            jump battle_sequence

    elif result == "run":
        hide screen battle_interface
        "You try to escape, but the creature blocks you!"
        jump battle_sequence

label victory:
    "Victory is yours! The creature flees, terrified by [player_creature]'s aggression."
    $ friendship -= 1
    "You continue your journey, but your creature doesn't seem very happy..."
    jump companion_backstory

label friendship:
    "Maybe the real victory was the friends we made along the way."
    "Perhaps now you can journey together..."
    $ friendship += 2
    jump companion_backstory
