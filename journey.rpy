# Getting to Know Our Creature Companion

label companion_backstory:
    scene bg forest with dissolve
    "You travel on in the woods for a while in silence"
    m "Now that we're past that...who are you?"
    if player_creature == "Jackalope":
        jump jackalope_dialogue
    elif player_creature == "Mothkid":
        jump mothkid_dialogue
    elif player_creature == "Hypnotoad":
        jump hypnotoad_dialogue

label jackalope_dialogue:
    show jackalope: 
        xalign 0.1 
        yalign 0.6
    if friendship >= 5:
        c "I'm Jackalope. I've been hopping through enchanted forests since forever. I've witnessed mystical glades and hidden groves, and I trust you enough now to share my full story."
    else:
        c "Hey, I'm Jackalope. Some things are best left unspoken..."
    return

label mothkid_dialogue:
    show mothkid: 
        xalign 0.1
        yalign 0.6
    if friendship >= 5:
        c "I'm Mothkid. Born under the silver glow of the moon, I fluttered through nights filled with whispered legends and ancient secrets. I feel comfortable enough with you to reveal my past."
    else:
        c "I'm Mothkid. There's not much to say about my past right now..."
    return

label hypnotoad_dialogue:
    show hypnotoad: 
        xalign 0.1
        yalign 0.6
    if friendship >= 5:
        c "Ribbit. I'm Hypnotoad. My mesmerizing gaze has seen surreal nights and murky swamps teeming with secrets. Since we’re pals now, I’ll let you in on my story."
    else:
        c "Some tales are better left to the shadows..."
    return