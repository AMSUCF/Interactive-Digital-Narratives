screen suspicion_meter():
    frame:
        xalign 0.05 yalign 0.02
        text "Suspicion: [suspicion]"

screen inventory():
    frame:
        xalign 0.95 yalign 0.02
        if inventory:
            text "Inventory: [', '.join(inventory)]"
        else:
            text "Inventory: Empty"

define s = Character("Mary", color="#c8ffc8")
define m = Character("Me", color="#c8c8ff")
define x = Character("Max", color="#ffc8c8")

default suspicion = 0
default inventory = []

label start:

    show screen suspicion_meter
    show screen inventory
    play music background

    scene bg lecturehall
    with fade

    "The usual chatter of students fades as I stare at the empty seat in the front row."
    "It belongs to Ryan. He never missed a class." 
    "But today, he's missing. And not just from class."

    scene bg uni
    with fade

    "Outside, the campus is abuzz with whispers. A body was found near the library."
    "Ryan's body."

    "I spot Mary standing near the edge of the crowd. Her expression unreadable."

    show mary
    with dissolve

    m "Mary... did you hear? About Ryan?"

    s "Yeah... I can't believe it. He was just here yesterday."

    menu:
        "Ask where she was last night":
            jump question_alibi
        "Say nothing for now":
            jump investigate_scene

label question_alibi:
    s "I was at home, studying. Why? Do you think I had something to do with this?"
    menu:
        "Say it's just a question":
            m "No, I'm just trying to piece things together."
            jump investigate_scene
        "Press her for details":
            $ suspicion += 1
            m "You don’t seem too surprised. Are you sure you weren’t there?"
            s "I told you. I was home. Alone."
            jump investigate_scene

label investigate_scene:
    scene bg library
    with fade

    "The area near the library is taped off. Police are everywhere."

    show bracelet
    with dissolve
    "I notice something on a shelf — a bracelet. I recognize it."

    menu:
        "Take the bracelet discreetly":
            $ suspicion += 1
            $ inventory.append("Bracelet")
            hide bracelet
            jump confront_mary
        "Leave it and report it to the police":
            hide bracelet
            jump final_decision

label confront_mary:
    scene bg uni
    show mary
    with fade

    m "Mary, I found this near the crime scene. It’s yours, isn’t it?"
    s "...That doesn’t mean anything. I lost it yesterday."

    if suspicion >= 2:
        jump accuse_mary
    else:
        jump final_decision

label accuse_mary:
    s "I can’t believe you think I did this."
    m "Then explain the bracelet."
    s "Fine. I was there. But I didn’t kill him! I saw someone else... I was scared."
    m "Who?"
    s "It was Max. He was arguing with Ryan. Then I ran."

    "A new suspect. Time to find Max."
    jump confront_max

label confront_max:
    scene bg campus_night
    show max
    with fade

    m "Max. I need to talk to you."
    x "About Ryan? Look, I didn't mean for anything to happen."

    menu:
        "Press Max for details":
            m "You were seen arguing with him. What happened?"
            x "He knew something about me. I... I had to stop him."
            jump max_confession
        "Let the police handle it":
            "I step back, knowing the truth will come out soon enough."
            return

label max_confession:
    "Max exhales shakily."
    x "I didn’t mean to hurt him. It was an accident. I just wanted him to back off."
    "The truth is out. Justice will be served."
    return

label final_decision:
    "The police take the bracelet as evidence."
    "Whether Mary is guilty or not, the truth will come out soon."
    return
